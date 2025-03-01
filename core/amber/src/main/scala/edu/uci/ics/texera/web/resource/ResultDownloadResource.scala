package edu.uci.ics.texera.web.resource

import com.google.api.client.googleapis.json.GoogleJsonResponseException
import com.google.api.client.util.Lists
import com.google.api.services.drive.Drive
import com.google.api.services.drive.model.{File, FileList, Permission}
import com.google.api.services.sheets.v4.Sheets
import com.google.api.services.sheets.v4.model.{Spreadsheet, SpreadsheetProperties, ValueRange}
import edu.uci.ics.amber.engine.common.tuple.ITuple
import edu.uci.ics.texera.web.model.event.ResultDownloadResponse
import edu.uci.ics.texera.web.model.request.ResultDownloadRequest
import edu.uci.ics.texera.web.resource.WorkflowWebsocketResource.{
  sessionDownloadCache,
  sessionResults
}
import edu.uci.ics.texera.workflow.common.tuple.Tuple
import edu.uci.ics.texera.workflow.common.Utils.retry

import java.util
import java.util.concurrent.{Executors, ThreadPoolExecutor}
import scala.annotation.tailrec
import scala.collection.JavaConverters._
import scala.collection.mutable
import scala.util.{Failure, Success, Try}
object ResultDownloadResource {

  private final val UPLOAD_BATCH_ROW_COUNT = 10000
  private final val RETRY_ATTEMPTS = 7
  private final val BASE_BACK_OOF_TIME_IN_MS = 1000
  private final val WORKFLOW_RESULT_FOLDER_NAME = "workflow_results"
  private final val pool: ThreadPoolExecutor =
    Executors.newFixedThreadPool(3).asInstanceOf[ThreadPoolExecutor]
  @volatile private var WORKFLOW_RESULT_FOLDER_ID: String = _

  def apply(
      sessionId: String,
      request: ResultDownloadRequest
  ): ResultDownloadResponse = {
    // retrieve the file link saved in the session if exists
    if (
      sessionDownloadCache.contains(sessionId) && sessionDownloadCache(sessionId).contains(
        request.downloadType
      )
    ) {
      return ResultDownloadResponse(
        request.downloadType,
        sessionDownloadCache(sessionId)(request.downloadType),
        "File retrieved from cache."
      )
    }

    // By now the workflow should finish running. Only one operator should contain results
    // TODO: currently assume only one operator should contains the result
    // TODO: change status checking of the workflow
    val operatorWithResult =
      sessionResults(sessionId).operatorResults.values.count(p => p.getResult.nonEmpty)
    if (operatorWithResult == 0) {
      return ResultDownloadResponse(
        request.downloadType,
        "",
        "The workflow contains no results"
      )
    } else if (operatorWithResult > 1) {
      // more than one operator contains results means the workflow does not finish running.
      return ResultDownloadResponse(
        request.downloadType,
        "",
        "The workflow does not finish running"
      )
    }

    // convert the ITuple into tuple
    // TODO: currently only accept the tuple as input
    val results: List[Tuple] =
      sessionResults(sessionId).operatorResults.values
        .find(p => p.getResult.nonEmpty)
        .get
        .getResult
        .map(iTuple => iTuple.asInstanceOf[Tuple])
    val schema = getSchema(results.head)

    // handle the request according to download type
    var response: ResultDownloadResponse = null
    request.downloadType match {
      case "google_sheet" =>
        response = handleGoogleSheetRequest(request, results, schema)
      case _ =>
        response = ResultDownloadResponse(
          request.downloadType,
          "",
          s"Unknown download type: ${request.downloadType}"
        )
    }

    // save the file link in the session cache
    if (!sessionDownloadCache.contains(sessionId)) {
      sessionDownloadCache.put(
        sessionId,
        mutable.HashMap(request.downloadType -> response.link)
      )
    } else {
      sessionDownloadCache(sessionId)
        .put(request.downloadType, response.link)
    }

    response
  }

  // get the schema from the sample tuple
  private def getSchema(tuple: Tuple): util.List[AnyRef] = {
    tuple.getSchema.getAttributeNames
      .asInstanceOf[util.List[AnyRef]]
  }

  private def handleGoogleSheetRequest(
      resultDownloadRequest: ResultDownloadRequest,
      result: List[ITuple],
      schema: util.List[AnyRef]
  ): ResultDownloadResponse = {
    // create google sheet
    val sheetService: Sheets = GoogleResource.getSheetService
    val sheetId: String =
      createGoogleSheet(sheetService, resultDownloadRequest.workflowName)
    if (sheetId == null)
      return ResultDownloadResponse(
        resultDownloadRequest.downloadType,
        "",
        "Fail to create google sheet"
      )

    val driveService: Drive = GoogleResource.getDriveService
    moveToResultFolder(driveService, sheetId)

    // allow user to access this sheet in the service account
    val sharePermission: Permission = new Permission()
      .setType("anyone")
      .setRole("reader")
    driveService
      .permissions()
      .create(sheetId, sharePermission)
      .execute()

    // upload the content asynchronously to avoid long waiting on the user side.
    pool
      .submit(() =>
        {
          uploadHeader(sheetService, sheetId, schema)
          uploadResult(sheetService, sheetId, result)
        }.asInstanceOf[Runnable]
      )

    // generate success response
    val link: String = s"https://docs.google.com/spreadsheets/d/$sheetId/edit"
    val message: String =
      s"Google sheet created. The results may be still uploading."
    ResultDownloadResponse(resultDownloadRequest.downloadType, link, message)
  }

  /**
    * create the google sheet and return the sheet Id
    */
  private def createGoogleSheet(sheetService: Sheets, workflowName: String): String = {
    val createSheetRequest = new Spreadsheet()
      .setProperties(new SpreadsheetProperties().setTitle(workflowName))
    val targetSheet: Spreadsheet = sheetService.spreadsheets
      .create(createSheetRequest)
      .setFields("spreadsheetId")
      .execute
    targetSheet.getSpreadsheetId
  }

  /**
    * move the workflow results to a specific folder
    */
  @tailrec
  private def moveToResultFolder(
      driveService: Drive,
      sheetId: String,
      retry: Boolean = true
  ): Unit = {
    Try(
      driveService
        .files()
        .update(sheetId, null)
        .setAddParents(WORKFLOW_RESULT_FOLDER_ID)
        .execute()
    ) match {
      case Success(_) => // do nothing upon success
      case Failure(exception: GoogleJsonResponseException) =>
        if (retry) {
          // This exception maybe caused by the full deletion of the target folder and
          // the cached folder id is obsolete.
          //  * note: by full deletion, the folder has to be deleted from trash as well.
          // In this case, retrieve the folder id to try again.
          retrieveResultFolderId(driveService)
          moveToResultFolder(driveService, sheetId, retry = false)
        } else {
          // if the exception continues to show up then just throw it normally.
          throw exception
        }
    }
  }

  private def retrieveResultFolderId(driveService: Drive): String =
    synchronized {

      val folderResult: FileList = driveService
        .files()
        .list()
        .setQ(
          s"mimeType = 'application/vnd.google-apps.folder' and name='${WORKFLOW_RESULT_FOLDER_NAME}'"
        )
        .setSpaces("drive")
        .execute()

      if (folderResult.getFiles.isEmpty) {
        val fileMetadata: File = new File()
        fileMetadata.setName(WORKFLOW_RESULT_FOLDER_NAME)
        fileMetadata.setMimeType("application/vnd.google-apps.folder")
        val targetFolder: File = driveService.files.create(fileMetadata).setFields("id").execute
        WORKFLOW_RESULT_FOLDER_ID = targetFolder.getId
      } else {
        WORKFLOW_RESULT_FOLDER_ID = folderResult.getFiles.get(0).getId
      }
      WORKFLOW_RESULT_FOLDER_ID
    }

  /**
    * upload the result header to the google sheet
    */
  private def uploadHeader(
      sheetService: Sheets,
      sheetId: String,
      schema: util.List[AnyRef]
  ): Unit = {
    val schemaContent: util.List[util.List[AnyRef]] = Lists.newArrayList()
    schemaContent.add(schema)
    uploadContent(sheetService, sheetId, schemaContent)
  }

  /**
    * upload the result body to the google sheet
    */
  private def uploadResult(sheetService: Sheets, sheetId: String, result: List[ITuple]): Unit = {
    val content: util.List[util.List[AnyRef]] =
      Lists.newArrayListWithCapacity(UPLOAD_BATCH_ROW_COUNT)
    // use for loop to avoid copying the whole result at the same time
    for (tuple: ITuple <- result) {

      val tupleContent: util.List[AnyRef] =
        tuple
          .asInstanceOf[Tuple]
          .getFields
          .stream()
          .map(convertUnsupported)
          .toArray
          .toList
          .asJava
      content.add(tupleContent)

      if (content.size() == UPLOAD_BATCH_ROW_COUNT) {
        uploadContent(sheetService, sheetId, content)
        content.clear()
      }
    }

    if (!content.isEmpty) {
      uploadContent(sheetService, sheetId, content)
    }
  }

  /**
    * convert the tuple content into the type the Google Sheet API supports
    */
  private def convertUnsupported(content: AnyRef): AnyRef = {
    content match {

      // if null, use empty string to represent.
      case null => ""

      // Google Sheet API supports String and number(long, int, double and so on)
      case _: String | _: Number => content

      // convert all the other type into String
      case _ => content.toString
    }

  }

  /**
    * upload the content to the google sheet
    * The type of content is java list because the google API is in java
    */
  private def uploadContent(
      sheetService: Sheets,
      sheetId: String,
      content: util.List[util.List[AnyRef]]
  ): Unit = {
    val body: ValueRange = new ValueRange().setValues(content)
    val range: String = "A1"
    val valueInputOption: String = "RAW"

    // using retry logic here, to handle possible API errors, i.e., rate limit exceeded.
    retry(attempts = RETRY_ATTEMPTS, baseBackoffTimeInMS = BASE_BACK_OOF_TIME_IN_MS) {
      sheetService.spreadsheets.values
        .append(sheetId, range, body)
        .setValueInputOption(valueInputOption)
        .execute
    }

  }
}

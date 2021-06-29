// Generated by the Scala Plugin for the Protocol Buffer Compiler.
// Do not edit!
//
// Protofile syntax: PROTO3

package edu.uci.ics.amber.engine.architecture.worker.promisehandler2

object Promisehandler2Proto extends _root_.scalapb.GeneratedFileObject {
  lazy val dependencies: Seq[_root_.scalapb.GeneratedFileObject] = Seq(
    edu.uci.ics.amber.engine.architecture.sendsemantics.datatransferpolicy2.Datatransferpolicy2Proto,
    edu.uci.ics.amber.engine.common.virtualidentity.VirtualidentityProto
  )
  lazy val messagesCompanions: Seq[_root_.scalapb.GeneratedMessageCompanion[_ <: _root_.scalapb.GeneratedMessage]] =
    Seq[_root_.scalapb.GeneratedMessageCompanion[_ <: _root_.scalapb.GeneratedMessage]](
      edu.uci.ics.amber.engine.architecture.worker.promisehandler2.StartWorker,
      edu.uci.ics.amber.engine.architecture.worker.promisehandler2.UpdateInputLinking,
      edu.uci.ics.amber.engine.architecture.worker.promisehandler2.AddOutputPolicy,
      edu.uci.ics.amber.engine.architecture.worker.promisehandler2.ControlCommandMessage
    )
  private lazy val ProtoBytes: _root_.scala.Array[Byte] =
      scalapb.Encoding.fromBase64(scala.collection.immutable.Seq(
  """CkJlZHUvdWNpL2ljcy9hbWJlci9lbmdpbmUvYXJjaGl0ZWN0dXJlL3dvcmtlci9wcm9taXNlaGFuZGxlcjIucHJvdG8SLGVkd
  S51Y2kuaWNzLmFtYmVyLmVuZ2luZS5hcmNoaXRlY3R1cmUud29ya2VyGk1lZHUvdWNpL2ljcy9hbWJlci9lbmdpbmUvYXJjaGl0Z
  WN0dXJlL3NlbmRzZW1hbnRpY3MvZGF0YXRyYW5zZmVycG9saWN5Mi5wcm90bxo1ZWR1L3VjaS9pY3MvYW1iZXIvZW5naW5lL2Nvb
  W1vbi92aXJ0dWFsaWRlbnRpdHkucHJvdG8iDQoLU3RhcnRXb3JrZXIi2QEKElVwZGF0ZUlucHV0TGlua2luZxJmCgppZGVudGlma
  WVyGAEgASgLMjUuZWR1LnVjaS5pY3MuYW1iZXIuZW5naW5lLmNvbW1vbi5BY3RvclZpcnR1YWxJZGVudGl0eUIP4j8MEgppZGVud
  GlmaWVyUgppZGVudGlmaWVyElsKCWlucHV0TGluaxgCIAEoCzItLmVkdS51Y2kuaWNzLmFtYmVyLmVuZ2luZS5jb21tb24uTGlua
  0lkZW50aXR5Qg7iPwsSCWlucHV0TGlua1IJaW5wdXRMaW5rIn4KD0FkZE91dHB1dFBvbGljeRJrCgZwb2xpY3kYASABKAsyRi5lZ
  HUudWNpLmljcy5hbWJlci5lbmdpbmUuYXJjaGl0ZWN0dXJlLnNlbmRzZW1hbnRpY3MuRGF0YVNlbmRpbmdQb2xpY3lCC+I/CBIGc
  G9saWN5UgZwb2xpY3kioAMKDkNvbnRyb2xDb21tYW5kEn8KD2FkZE91dHB1dFBvbGljeRgDIAEoCzI9LmVkdS51Y2kuaWNzLmFtY
  mVyLmVuZ2luZS5hcmNoaXRlY3R1cmUud29ya2VyLkFkZE91dHB1dFBvbGljeUIU4j8REg9hZGRPdXRwdXRQb2xpY3lIAFIPYWRkT
  3V0cHV0UG9saWN5Em8KC3N0YXJ0V29ya2VyGAQgASgLMjkuZWR1LnVjaS5pY3MuYW1iZXIuZW5naW5lLmFyY2hpdGVjdHVyZS53b
  3JrZXIuU3RhcnRXb3JrZXJCEOI/DRILc3RhcnRXb3JrZXJIAFILc3RhcnRXb3JrZXISiwEKEnVwZGF0ZUlucHV0TGlua2luZxgFI
  AEoCzJALmVkdS51Y2kuaWNzLmFtYmVyLmVuZ2luZS5hcmNoaXRlY3R1cmUud29ya2VyLlVwZGF0ZUlucHV0TGlua2luZ0IX4j8UE
  hJ1cGRhdGVJbnB1dExpbmtpbmdIAFISdXBkYXRlSW5wdXRMaW5raW5nQg4KDHNlYWxlZF92YWx1ZWIGcHJvdG8z"""
      ).mkString)
  lazy val scalaDescriptor: _root_.scalapb.descriptors.FileDescriptor = {
    val scalaProto = com.google.protobuf.descriptor.FileDescriptorProto.parseFrom(ProtoBytes)
    _root_.scalapb.descriptors.FileDescriptor.buildFrom(scalaProto, dependencies.map(_.scalaDescriptor))
  }
  lazy val javaDescriptor: com.google.protobuf.Descriptors.FileDescriptor = {
    val javaProto = com.google.protobuf.DescriptorProtos.FileDescriptorProto.parseFrom(ProtoBytes)
    com.google.protobuf.Descriptors.FileDescriptor.buildFrom(javaProto, _root_.scala.Array(
      edu.uci.ics.amber.engine.architecture.sendsemantics.datatransferpolicy2.Datatransferpolicy2Proto.javaDescriptor,
      edu.uci.ics.amber.engine.common.virtualidentity.VirtualidentityProto.javaDescriptor
    ))
  }
  @deprecated("Use javaDescriptor instead. In a future version this will refer to scalaDescriptor.", "ScalaPB 0.5.47")
  def descriptor: com.google.protobuf.Descriptors.FileDescriptor = javaDescriptor
}
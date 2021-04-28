package edu.uci.ics.amber.engine.recovery

class InputCounter {
  private var enabled = false
  private var dataDisabled = false
  private var dataInputCount = 0L
  private var controlInputCount = 0L

  def advanceDataInputCount(): Unit = {
    if (enabled && !dataDisabled) dataInputCount += 1
  }

  def advanceControlInputCount(): Unit = {
    if (enabled) controlInputCount += 1
  }

  def enable(): Unit = {
    enabled = true
  }

  def disableDataCount():Unit = {
    dataDisabled = true
  }

  def getDataInputCount: Long = dataInputCount

  def getControlInputCount: Long = controlInputCount
}

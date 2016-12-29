##########################################################################
# Author:               Eduardo Crispim, emcrispim@gmail.com
# Date:                 December, 2016
# 
# This program is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License version 2 or (at your
# option) any later version as published by the Free Software Foundation.
#
#########################################################################

from Products.Zuul.form import schema
from Products.Zuul.interfaces.device import IDeviceInfo
from Products.Zuul.interfaces.component import IComponentInfo
from Products.Zuul.utils import ZuulMessageFactory as _t

class IEnclosureInfo(IComponentInfo):
  id = schema.TextLine(title=_t('Enclosure ID'))
  status = schema.TextLine(title=_t('Status'))
  slot = schema.TextLine(title=_t('Slot'))
  parentslot = schema.TextLine(title=_t('Parent Slot'))
  relativeslot = schema.TextLine(title=_t('Relative Slot'))
  alarmcontrol = schema.TextLine(title=_t('Alarm Control'))
  failure = schema.TextLine(title=_t('Failure'))
  warning = schema.TextLine(title=_t('Warning'))
  sn = schema.TextLine(title=_t('SN'))
  pn = schema.TextLine(title=_t('PN'))
  controllerenclosure = schema.TextLine(title=_t('Controller Enclosure'))

class IControllerInfo(IComponentInfo):
  id = schema.TextLine(title=_t('Controller ID'))
  status = schema.TextLine(title=_t('Status'))
  slot = schema.TextLine(title=_t('Slot'))
  parentslot = schema.TextLine(title=_t('Parent Slot'))
  relativeslot = schema.TextLine(title=_t('Relative Slot'))
  sn = schema.TextLine(title=_t('SN'))
  pn = schema.TextLine(title=_t('PN'))
  alarmcontrol = schema.TextLine(title=_t('Alarm Control'))
  enclosureid = schema.TextLine(title=_t('Enclosure ID'))
  ctype = schema.TextLine(title=_t('Type'))

class IBatteryInfo(IComponentInfo):
  id = schema.TextLine(title=_t('Battery ID'))
  status = schema.TextLine(title=_t('Status'))
  slot = schema.TextLine(title=_t('Slot'))
  parentslot = schema.TextLine(title=_t('Parent Slot'))
  relativeslot = schema.TextLine(title=_t('Relative Slot'))
  sn = schema.TextLine(title=_t('SN'))
  pn = schema.TextLine(title=_t('PN'))
  alarmcontrol = schema.TextLine(title=_t('Alarm Control'))
  installationtime = schema.TextLine(title=_t('Installation Time'))
  expirationtime = schema.TextLine(title=_t('Expiration Time'))

class ITempSensorInfo(IComponentInfo):
  id = schema.TextLine(title=_t('Battery ID'))
  status = schema.TextLine(title=_t('Status'))
  slot = schema.TextLine(title=_t('Slot'))
  parentslot = schema.TextLine(title=_t('Parent Slot'))
  relativeslot = schema.TextLine(title=_t('Relative Slot'))
  alarmcontrol = schema.TextLine(title=_t('Alarm Control'))


class ISCSIPortInfo(IComponentInfo):
  id = schema.TextLine(title=_t('SCSI Port ID'))
  status = schema.TextLine(title=_t('Status'))
  slot = schema.TextLine(title=_t('Slot'))
  parentslot = schema.TextLine(title=_t('Parent Slot'))
  relativeslot = schema.TextLine(title=_t('Relative Slot'))
  alarmcontrol = schema.TextLine(title=_t('Alarm Control'))
  lostlink = schema.TextLine(title=_t('Lost Link'))

class IPowerSupplyInfo(IComponentInfo):
  id = schema.TextLine(title=_t('Power Supply Port ID'))
  status = schema.TextLine(title=_t('Status'))
  slot = schema.TextLine(title=_t('Slot'))
  parentslot = schema.TextLine(title=_t('Parent Slot'))
  relativeslot = schema.TextLine(title=_t('Relative Slot'))
  sn = schema.TextLine(title=_t('SN'))
  pn = schema.TextLine(title=_t('PN'))
  alarmcontrol = schema.TextLine(title=_t('Alarm Control'))
  fanstatus = schema.TextLine(title=_t('Fan Status'))
  powersupplystatus = schema.TextLine(title=_t('Power Supply Status'))
  haspowerinput = schema.TextLine(title=_t('Has Power Input?'))
  tempsensorstatus = schema.Int(title=_t('Temperature Status'))
  temperature = schema.TextLine(title=_t('Temperature (C)'))

class IDriveInfo(IComponentInfo):
  id = schema.TextLine(title=_t('Power Supply Port ID'))
  status = schema.TextLine(title=_t('Status'))
  slot = schema.TextLine(title=_t('Slot'))
  parentslot = schema.TextLine(title=_t('Parent Slot'))
  relativeslot = schema.TextLine(title=_t('Relative Slot'))
  alarmcontrol = schema.TextLine(title=_t('Alarm Control'))
  wwn = schema.TextLine(title=_t('WWN'))
  drivetype = schema.TextLine(title=_t('Drive Type'))
  faultsensed = schema.TextLine(title=_t('Fault Sensed?'))
  trayid = schema.TextLine(title=_t('Enclosure ID'))
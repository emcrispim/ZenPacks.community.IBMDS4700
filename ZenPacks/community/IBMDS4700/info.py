##########################################################################
# Author:               Eduardo Crispim, emcrispim@gmail.com
# Date:                 December, 2016
# 
# This program is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License version 2 or (at your
# option) any later version as published by the Free Software Foundation.
#
#########################################################################

from zope.interface import implements

from Products.Zuul.infos import ProxyProperty
from Products.Zuul.infos.device import DeviceInfo
from Products.Zuul.infos.component import ComponentInfo

from ZenPacks.community.IBMDS4700.interfaces import (
    IEnclosureInfo,
    IControllerInfo,
    IBatteryInfo,
    ITempSensorInfo,
    ISCSIPortInfo,
    IPowerSupplyInfo,
    IDriveInfo,
    )


class EnclosureInfo(ComponentInfo):
    implements(IEnclosureInfo)

    id = ProxyProperty('id')
    status = ProxyProperty('status')
    slot = ProxyProperty('slot')
    parentslot = ProxyProperty('parentslot')
    relativeslot = ProxyProperty('relativeslot')
    alarmcontrol = ProxyProperty('alarmcontrol')
    failure = ProxyProperty('failure')
    warning = ProxyProperty('warning')
    sn = ProxyProperty('sn')
    pn = ProxyProperty('pn')
    controllerenclosure = ProxyProperty('controllerenclosure')

class ControllerInfo(ComponentInfo):
    implements(IControllerInfo)

    id = ProxyProperty('id')
    status = ProxyProperty('status')
    slot = ProxyProperty('slot')
    parentslot = ProxyProperty('parentslot')
    relativeslot = ProxyProperty('relativeslot')
    sn = ProxyProperty('sn')
    pn = ProxyProperty('pn')
    alarmcontrol = ProxyProperty('alarmcontrol')
    enclosureid = ProxyProperty('enclosureid')
    ctype = ProxyProperty('ctype')


class BatteryInfo(ComponentInfo):
    implements(IBatteryInfo)

    id = ProxyProperty('id')
    status = ProxyProperty('status')
    slot = ProxyProperty('slot')
    parentslot = ProxyProperty('parentslot')
    relativeslot = ProxyProperty('relativeslot')
    sn = ProxyProperty('sn')
    pn = ProxyProperty('pn')
    alarmcontrol = ProxyProperty('alarmcontrol')
    installationtime = ProxyProperty('installationtime')
    expirationtime = ProxyProperty('expirationtime')

class TempSensorInfo(ComponentInfo):
    implements(ITempSensorInfo)

    id = ProxyProperty('id')
    status = ProxyProperty('status')
    slot = ProxyProperty('slot')
    parentslot = ProxyProperty('parentslot')
    relativeslot = ProxyProperty('relativeslot')
    alarmcontrol = ProxyProperty('alarmcontrol')


class SCSIPortInfo(ComponentInfo):
    implements(ISCSIPortInfo)

    id = ProxyProperty('id')
    status = ProxyProperty('status')
    slot = ProxyProperty('slot')
    parentslot = ProxyProperty('parentslot')
    relativeslot = ProxyProperty('relativeslot')
    alarmcontrol = ProxyProperty('alarmcontrol')
    lostlink = ProxyProperty('lostlink')
    transmitfailed = ProxyProperty('transmitfailed')

class PowerSupplyInfo(ComponentInfo):
    implements(IPowerSupplyInfo)

    id = ProxyProperty('id')
    status = ProxyProperty('status')
    slot = ProxyProperty('slot')
    parentslot = ProxyProperty('parentslot')
    relativeslot = ProxyProperty('relativeslot')
    alarmcontrol = ProxyProperty('alarmcontrol')
    sn = ProxyProperty('sn')
    pn = ProxyProperty('pn')
    alarmcontrol = ProxyProperty('alarmcontrol')
    fanstatus = ProxyProperty('fanstatus')
    powersupplystatus = ProxyProperty('powersupplystatus')
    haspowerinput = ProxyProperty('haspowerinput')
    tempsensorstatus = ProxyProperty('tempsensorstatus')
    temperature = ProxyProperty('temperature')
    
class DriveInfo(ComponentInfo):
    implements(IDriveInfo)

    id = ProxyProperty('id')
    status = ProxyProperty('status')
    slot = ProxyProperty('slot')
    parentslot = ProxyProperty('parentslot')
    relativeslot = ProxyProperty('relativeslot')
    alarmcontrol = ProxyProperty('alarmcontrol')
    wwn = ProxyProperty('wwn')
    drivetype = ProxyProperty('drivetype')
    faultsensed = ProxyProperty('faultsensed')
    fanstatus = ProxyProperty('fanstatus')
    trayid = ProxyProperty('trayid')
##########################################################################
# Author:               Eduardo Crispim, emcrispim@gmail.com
# Date:                 December, 2016
# 
# This program is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License version 2 or (at your
# option) any later version as published by the Free Software Foundation.
#
#########################################################################

from Products.ZenRRD.CommandParser import CommandParser
from Products.ZenUtils.ZenScriptBase import ZenScriptBase
from ZenPacks.community.IBMDS4700 import Utils
from transaction import commit

class monitorParser(CommandParser):

  def processResults(self, cmd, result):
    scriptbase = ZenScriptBase(noopts = 1, connect = True)
    devname = cmd.deviceConfig.device
    device = scriptbase.findDevice(devname)

    data = Utils.telnetClient(
        device.zTelnetLoginRegex,
        cmd.deviceConfig.zCommandCommandTimeout,
        device.zTelnetPasswordRegex,
        cmd.deviceConfig.zCommandUsername,
        cmd.deviceConfig.zCommandPassword,
        cmd.deviceConfig.manageIp
    )
    data = Utils.xmlencode(data)
    data = Utils.processxml(data,device)

    for e in data['enclosures']:
        if e.failure!='No' or e.status!='Okay' or e.alarmcontrol!='Off' or e.warning!='No':
            cmd.component = e.id
            result.events.append(Utils.getEvent(cmd,"Enclosure failure",clear=False))
        component = device.enclosure.findObjectsById(e.id)[0]
        component.failure = e.failure
        component.status = e.status
        component.alarmcontrol = e.alarmcontrol
        component.warning = e.warning

    for e in data['supportCRUs']:
        if e.status!='Okay' or e.alarmcontrol!='Off' or e.fanstatus!='Okay' or e.powersupplystatus!='Okay' or e.tempsensorstatus!='Okay':
            cmd.component = e.id
            result.events.append(Utils.getEvent(cmd,"Power Supply failure",clear=False))
        component = device.powersupply.findObjectsById(e.id)[0]
        component.status = e.status
        component.alarmcontrol = e.alarmcontrol
        component.fanstatus = e.fanstatus
        component.powersupplystatus = e.powersupplystatus
        component.tempsensorstatus = e.tempsensorstatus

    for e in data['drives']:
        if e.status!='Okay' or e.alarmcontrol!='Off' or e.faultsensed!='No':
            cmd.component = e.id
            result.events.append(Utils.getEvent(cmd,"Drive failure",clear=False))
        component = device.drive.findObjectsById(e.id)[0]
        component.status = e.status
        component.alarmcontrol = e.alarmcontrol
        component.faultsensed = e.faultsensed

    for e in data['scsiports']:
        if (e.status!='Okay' and e.status!='Missing') or e.alarmcontrol!='Off' or e.lostlink!='No' or e.transmitfailed!='No':
            cmd.component = e.id
            result.events.append(Utils.getEvent(cmd,"SCSI Port failure",clear=False))
        component = device.scsiport.findObjectsById(e.id)[0]
        component.status = e.status
        component.alarmcontrol = e.alarmcontrol
        component.lostlink = e.lostlink
        component.transmitfailed = e.transmitfailed

    for e in data['batteries']:
        if e.status!='Okay':
            cmd.component = e.id
            result.events.append(Utils.getEvent(cmd,"Battery failure",clear=False))
        component = device.battery.findObjectsById(e.id)[0]
        component.status = e.status
        
    for e in data['controllers']:
        if e.status!='Okay' or e.alarmcontrol!='Off':
            cmd.component = e.id
            result.events.append(Utils.getEvent(cmd,"Controller failure",clear=False))
        component = device.controller.findObjectsById(e.id)[0]
        component.status = e.status
        component.alarmcontrol = e.alarmcontrol

    for e in data['tempsensors']:
        if e.status!='Okay' or e.alarmcontrol!='Off':
            cmd.component = e.id
            result.events.append(Utils.getEvent(cmd,"Temperature Sensor failure",clear=False))
        component = device.tempsensor.findObjectsById(e.id)[0]
        component.status = e.status
        component.alarmcontrol = e.alarmcontrol






    #result.events.append(Utils.getEvent(cmd,"teste",clear = False))
     
    """
    Process the results for command "lsenclosurebattery -delim :".
    """
    # datapointMap = dict([(dp.id, dp) for dp in cmd.points])
    # devname = cmd.deviceConfig.device
    # # returned from datasource component field with ${here/id}
    # componentid = cmd.component

    # rresult = Utils.cmdParser(cmd.result.output,'battery_id','BAT_ID')

    # # specific component device
    # rresult = rresult[componentid] 

    
    # # recondition_needed raise event
    # if rresult['recondition_needed']!='no': 
    #   result.events.append(Utils.getEvent(cmd,"Battery recondition needed",clear=False))

    # #Battery end of life warning raise event
    # if rresult['end_of_life_warning']!='no': 
    #   result.events.append(Utils.getEvent(cmd,"Battery end of life warning",clear=False))

    
    # # update current component
    # # zencommand does not have direct access to the model and components but
    # # maybe theres another way to do this
    
    # scriptbase = ZenScriptBase(noopts = 1, connect = True)
    # device = scriptbase.findDevice(devname)
    # component = device.batteries.findObjectsById(componentid)[0]
    # component.battery_status=rresult['status']
    # component.charging_status=rresult['charging_status']
    # component.recondition_needed=rresult['recondition_needed']
    # component.percent_charged=int(rresult['percent_charged'])
    # component.end_of_life_warning=rresult['end_of_life_warning']
    # commit()

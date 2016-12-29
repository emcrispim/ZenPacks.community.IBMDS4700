##########################################################################
# Author:               Eduardo Crispim, emcrispim@gmail.com
# Date:                 December, 2016
# 
# This program is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License version 2 or (at your
# option) any later version as published by the Free Software Foundation.
#
#########################################################################

import telnetlib
from  xml.dom.minidom import parseString
from Products.DataCollector.plugins.DataMaps import ObjectMap
import re

def telnetClient(zTelnetLoginRegex,zCommandCommandTimeout,zTelnetPasswordRegex,zCommandUsername,zCommandPassword,manageIp):
	t = telnetlib.Telnet(  )
	t.open(manageIp)	
	results = t.read_until(zTelnetLoginRegex,zCommandCommandTimeout)
	t.write(zCommandUsername+'\n')
	results = t.read_until(zTelnetPasswordRegex,zCommandCommandTimeout)
	t.write(zCommandPassword+'\n')
	results = t.read_until('-> ',zCommandCommandTimeout)
	t.write('ssmShowTree 2\n')
	results = t.read_until('-> ',zCommandCommandTimeout)
	return results


def xmlencode(results):
	def findText(l,sub):
			r  = ''
			for line in l.split("\n"):
				if sub in line:
					r +=line
			return r

	levelident=-1
	storage=''
	tags=[]

	for line in results.split("\r\n"):
		if len(findText(line,"[")):
			tag = line.split("[")[1].split("]")[0].replace(" ","")
			clevel = int(re.search('\S', line).start())
			if  clevel > levelident:
					
				tags.append([tag,clevel])
				storage+= "\n<%s>" % tag
			elif clevel == levelident:
				storage+= "</%s>" % tags.pop()[0]
				tags.append([tag,clevel])
				storage+= "\n<%s>" % tag

			else:
				storage+= "\n</%s>" % tags.pop()[0]
				if clevel == tags[len(tags)-1][1]:
					storage+= "\n</%s>" % tags.pop()[0]
				tags.append([tag,clevel])
				storage+= "\n<%s>" % tag

			levelident = clevel

		elif len(findText(line,"  Status:")):
			storage+= "\n<Status>%s</Status>" % line.split(':')[1].replace(" ","")
		elif len(findText(line,"devAddress:")):
			storage+= "\n<devAddress>%s</devAddress>" % line.split(':')[1].replace(" ","")
		elif len(findText(line,"Is Indicating Failure?:")):
			storage+= "\n<Failure>%s</Failure>" % line.split(':')[1].replace(" ","")
		elif len(findText(line,"Is Indicating Warning?:")):
			storage+= "\n<Warning>%s</Warning>" % line.split(':')[1].replace(" ","")
		elif len(findText(line,"  Slot:")):
			storage+= "\n<Slot>%s</Slot>" % line.split(':')[1].replace(" ","")
		elif len(findText(line,"Parent Slot:")):
			storage+= "\n<ParentSlot>%s</ParentSlot>" % line.split(':')[1].replace(" ","")
		elif len(findText(line,"Relative Slot:")):
			storage+= "\n<RelativeSlot>%s</RelativeSlot>" % line.split(':')[1].replace(" ","")
		elif len(findText(line,"|SN ")):
			storage+= "\n<SN>%s</SN>" % line.split('SN')[1].split('.')[0]
		elif len(findText(line,"|PN ")):
			storage+= "\n<PN>%s</PN>" % line.split('PN')[1].split('.')[0]
		elif len(findText(line,"driveType:")):
			storage+= "\n<driveType>%s</driveType>" % line.split(':')[1].replace(" ","")
		elif len(findText(line,"Alarm Count:")):
			storage+= "\n<AlarmCount>%s</AlarmCount>" % line.split(':')[1].replace(" ","")
		elif len(findText(line,"Alarm Control:")):
			storage+= "\n<AlarmControl>%s</AlarmControl>" % line.split(':')[1].replace(" ","")
		elif len(findText(line,"Controller Enclosure?:")):
			storage+= "\n<ControllerEnclosure>%s</ControllerEnclosure>" % line.split(':')[1].replace(" ","")
		elif len(findText(line,"Tray ID:")):
			storage+= "\n<TrayID>%s</TrayID>" % line.split(':')[1].replace(" ","")
		elif len(findText(line,"Installation Time:")):
			storage+= "\n<InstallationTime>%s</InstallationTime>" % line.split(':')[1].lstrip(' ')[0:10]
		elif len(findText(line,"Expiration Time:")):
			storage+= "\n<ExpirationTime>%s</ExpirationTime>" % line.split(':')[1].lstrip(' ')[0:10]
		elif len(findText(line,"Lost Link?:")):
			storage+= "\n<LostLink>%s</LostLink>" % line.split(':')[1].replace(" ","")
		elif len(findText(line,"Transmit Failed?:")):
			storage+= "\n<TransmitFailed>%s</TransmitFailed>" % line.split(':')[1].replace(" ","")
		elif len(findText(line,"Has Power Input?:")):
			storage+= "\n<HasPowerInput>%s</HasPowerInput>" % line.split(':')[1].replace(" ","")
		elif len(findText(line,"Temperature (C):")):
			storage+= "\n<Temperature>%s</Temperature>" % line.split(':')[1].replace(" ","")
		elif len(findText(line,"IEEE ID (WWN):")):
			storage+= "\n<WWN>%s</WWN>" % line.split(':')[1].replace(" ","")
		elif len(findText(line,"driveType:")):
			storage+= "\n<driveType>%s</driveType>" % line.split(':')[1].replace(" ","")
		elif len(findText(line,"Fault Sensed?:")):
			storage+= "\n<FaultSensed>%s</FaultSensed>" % line.split(':')[1].replace(" ","")
		
	for i in range(len(tags)):
		storage+= "</%s>" % tags.pop()[0]

	return  parseString(storage)

def processxml(results,device):
	xmlenclosures = results.getElementsByTagName('Enclosure')
	xmlcontrollers = []
	xmlbatteries = []
	xmltempsensor = []
	xmlscsiport = []
	xmlsupportCRU = []
	xmldrive = []
	enclosures = []
	controllers = []
	supportCRUs = []
	batteries = []
	tempsensors = []
	alarms = []
	drives = []
	scsiports = []

	for enc in xmlenclosures:
		for el in enc.childNodes:
			if el.nodeType == el.ELEMENT_NODE:
				if el.tagName == 'Status':
					Status = el.childNodes[0].nodeValue
				elif el.tagName == 'devAddress':
					devAddress = el.childNodes[0].nodeValue
				elif el.tagName == 'Slot':
					Slot = el.childNodes[0].nodeValue
				elif el.tagName == 'ParentSlot':
					ParentSlot = el.childNodes[0].nodeValue
				elif el.tagName == 'RelativeSlot':
					RelativeSlot= el.childNodes[0].nodeValue
				elif el.tagName == 'AlarmControl':
					AlarmControl= el.childNodes[0].nodeValue
				elif el.tagName == 'Failure':
					Failure= el.childNodes[0].nodeValue
				elif el.tagName == 'Warning':
					EWarning= el.childNodes[0].nodeValue
				elif el.tagName == 'SN':
					SN = el.childNodes[0].nodeValue
				elif el.tagName == 'PN':
					PN = el.childNodes[0].nodeValue
				elif el.tagName == 'Controller':
					xmlcontrollers.append([el,TrayID,'Controller'])
				elif el.tagName == 'ESM':
					xmlcontrollers.append([el,TrayID,'ESM'])
				elif el.tagName == 'SupportCRU':
					xmlsupportCRU.append(el)
				elif el.tagName == 'Alarm':
					alarms.append(el)
				elif el.tagName == 'Drive':
					xmldrive.append([el,TrayID])
				elif el.tagName == 'ControllerEnclosure':
					ControllerEnclosure = el.childNodes[0].nodeValue
				elif el.tagName == 'TrayID':
					TrayID = el.childNodes[0].nodeValue
			
		enclosures.append(ObjectMap(data={
			'id'					: device.prepId(TrayID),
			'title'					: TrayID,
			'status'				: Status,
			'slot'					: Slot,
			'parentslot'			: ParentSlot,
			'relativeslot'			: RelativeSlot,
			'alarmcontrol'			: AlarmControl,
			'failure'				: Failure,
			'warning'				: EWarning,
			'sn'					: SN,
			'pn'					: PN,
			'controllerenclosure' 	: ControllerEnclosure
			}))

	for con in xmlcontrollers:
		ccon    		= con[0]
		TrayID			= con[1]
		ControllerType  = con[2]
		for el in ccon.childNodes:
			if el.nodeType == el.ELEMENT_NODE:
				if el.tagName == 'devAddress':
						devAddress = el.childNodes[0].nodeValue
				elif el.tagName == 'Status':
						Status = el.childNodes[0].nodeValue
				elif el.tagName == 'Slot':
						Slot = el.childNodes[0].nodeValue
				elif el.tagName == 'ParentSlot':
						ParentSlot = el.childNodes[0].nodeValue
				elif el.tagName == 'RelativeSlot':
						RelativeSlot= el.childNodes[0].nodeValue
				elif el.tagName == 'SN':
						SN = el.childNodes[0].nodeValue
				elif el.tagName == 'PN':
						PN = el.childNodes[0].nodeValue
				elif el.tagName == 'AlarmControl':
						AlarmControl= el.childNodes[0].nodeValue
				elif el.tagName == 'Battery':
					xmlbatteries.append(el)
				elif el.tagName == 'TempSensor':
					xmltempsensor.append(el)
				elif el.tagName == 'SCSIPort':
					xmlscsiport.append(el)

		controllers.append(ObjectMap(data={
			'id'					:device.prepId(devAddress),
			'title'					:devAddress,
			'status'				:Status,
			'slot'					:Slot,
			'parentslot'			:ParentSlot,
			'relativeslot'			:RelativeSlot,
			'sn'					:SN,
			'pn'					:PN,
			'alarmcontrol'			:AlarmControl,
			'enclosureid'			:TrayID,
			'ctype' 				:ControllerType
			}))

	for bat in xmlbatteries:
		for el in bat.childNodes:
			if el.nodeType == el.ELEMENT_NODE:
				if el.tagName == 'devAddress':
						devAddress = el.childNodes[0].nodeValue
				elif el.tagName == 'Status':
						Status = el.childNodes[0].nodeValue
				elif el.tagName == 'Slot':
						Slot = el.childNodes[0].nodeValue
				elif el.tagName == 'ParentSlot':
						ParentSlot = el.childNodes[0].nodeValue
				elif el.tagName == 'RelativeSlot':
						RelativeSlot= el.childNodes[0].nodeValue
				elif el.tagName == 'SN':
						SN = el.childNodes[0].nodeValue
				elif el.tagName == 'PN':
						PN = el.childNodes[0].nodeValue
				elif el.tagName == 'AlarmControl':
						AlarmControl = el.childNodes[0].nodeValue
				elif el.tagName == 'InstallationTime':
						InstallationTime = el.childNodes[0].nodeValue
				elif el.tagName == 'ExpirationTime':
						ExpirationTime = el.childNodes[0].nodeValue

		batteries.append(ObjectMap(data={
			'id'					:device.prepId(devAddress),
			'title'					:devAddress,
			'status'				:Status,
			'slot'					:Slot,
			'parentslot'			:ParentSlot,
			'relativeslot'			:RelativeSlot,
			'sn'					:SN,
			'pn'					:PN,
			'alarmcontrol'			:AlarmControl,
			'installationtime'		:InstallationTime,
			'expirationtime' 		:ExpirationTime
			}))

	for tsens in xmltempsensor:
		for el in tsens.childNodes:
			if el.nodeType == el.ELEMENT_NODE:
				if el.tagName == 'devAddress':
						devAddress = el.childNodes[0].nodeValue
				elif el.tagName == 'Status':
						Status = el.childNodes[0].nodeValue
				elif el.tagName == 'Slot':
						Slot = el.childNodes[0].nodeValue
				elif el.tagName == 'ParentSlot':
						ParentSlot = el.childNodes[0].nodeValue
				elif el.tagName == 'RelativeSlot':
						RelativeSlot= el.childNodes[0].nodeValue
				elif el.tagName == 'AlarmControl':
						AlarmControl = el.childNodes[0].nodeValue

		tempsensors.append(ObjectMap(data={
			'id'					:device.prepId(devAddress),
			'title'					:devAddress,
			'status'				:Status,
			'slot'					:Slot,
			'parentslot'			:ParentSlot,
			'relativeslot'			:RelativeSlot,
			'alarmcontrol'			:AlarmControl
			}))

	for sport in xmlscsiport:
		for el in sport.childNodes:
			if el.nodeType == el.ELEMENT_NODE:
				if el.tagName == 'devAddress':
						devAddress = el.childNodes[0].nodeValue
				elif el.tagName == 'Status':
						Status = el.childNodes[0].nodeValue
				elif el.tagName == 'Slot':
						Slot = el.childNodes[0].nodeValue
				elif el.tagName == 'ParentSlot':
						ParentSlot = el.childNodes[0].nodeValue
				elif el.tagName == 'RelativeSlot':
						RelativeSlot= el.childNodes[0].nodeValue
				elif el.tagName == 'AlarmControl':
						AlarmControl = el.childNodes[0].nodeValue
				elif el.tagName == 'LostLink':
						LostLink = el.childNodes[0].nodeValue
				elif el.tagName == 'TransmitFailed':
						TransmitFailed = el.childNodes[0].nodeValue

		scsiports.append(ObjectMap(data={
			'id'					:device.prepId(devAddress),
			'title'					:devAddress,
			'status'				:Status,
			'slot'					:Slot,
			'parentslot'			:ParentSlot,
			'relativeslot'			:RelativeSlot,
			'alarmcontrol'			:AlarmControl,
			'lostlink'				:LostLink,
			'transmitfailed'		:TransmitFailed
			}))

	for ps in xmlsupportCRU:
		for el in ps.childNodes:
			if el.nodeType == el.ELEMENT_NODE:
				if el.tagName == 'devAddress':
						devAddress = el.childNodes[0].nodeValue
				elif el.tagName == 'Status':
						Status = el.childNodes[0].nodeValue
				elif el.tagName == 'Slot':
						Slot = el.childNodes[0].nodeValue
				elif el.tagName == 'ParentSlot':
						ParentSlot = el.childNodes[0].nodeValue
				elif el.tagName == 'RelativeSlot':
						RelativeSlot= el.childNodes[0].nodeValue
				elif el.tagName == 'SN':
						SN = el.childNodes[0].nodeValue
				elif el.tagName == 'PN':
						PN = el.childNodes[0].nodeValue
				elif el.tagName == 'AlarmControl':
						AlarmControl = el.childNodes[0].nodeValue
				elif el.tagName == 'Fan':
					FanStatus = el.getElementsByTagName('Status')[0].childNodes[0].nodeValue
				elif el.tagName == 'PowerSupply':
					PowerSupplyStatus = el.getElementsByTagName('Status')[0].childNodes[0].nodeValue
					HasPowerInput = el.getElementsByTagName('HasPowerInput')[0].childNodes[0].nodeValue
				elif el.tagName == 'TempSensor':
					TempSensorStatus = el.getElementsByTagName('Status')[0].childNodes[0].nodeValue
					Temperature = el.getElementsByTagName('Temperature')[0].childNodes[0].nodeValue
			
		supportCRUs.append(ObjectMap(data={
			'id'					:device.prepId(devAddress),
			'title'					:devAddress,
			'status'				:Status,
			'slot'					:Slot,
			'parentslot'			:ParentSlot,
			'relativeslot'			:RelativeSlot,
			'sn'					:SN,
			'pn'					:PN,
			'alarmcontrol'			:AlarmControl,
			'fanstatus'				:FanStatus,
			'powersupplystatus'		:PowerSupplyStatus,
			'haspowerinput'			:HasPowerInput,
			'tempsensorstatus'		:TempSensorStatus,
			'temperature'			:Temperature
			}))

	for drive in xmldrive:
		TrayID = drive[1]
		for el in drive[0].childNodes:
			if el.nodeType == el.ELEMENT_NODE:
				if el.tagName == 'devAddress':
						devAddress = el.childNodes[0].nodeValue
				elif el.tagName == 'Status':
						Status = el.childNodes[0].nodeValue
				elif el.tagName == 'Slot':
						Slot = el.childNodes[0].nodeValue
				elif el.tagName == 'ParentSlot':
						ParentSlot = el.childNodes[0].nodeValue
				elif el.tagName == 'RelativeSlot':
						RelativeSlot= el.childNodes[0].nodeValue
				elif el.tagName == 'AlarmControl':
						AlarmControl = el.childNodes[0].nodeValue
				elif el.tagName == 'WWN':
					WWN = el.childNodes[0].nodeValue
				elif el.tagName == 'driveType':
					driveType = el.childNodes[0].nodeValue
				elif el.tagName == 'FaultSensed':
					FaultSensed = el.childNodes[0].nodeValue
			
		drives.append(ObjectMap(data={
			'id'					:device.prepId(devAddress),
			'trayid'				:TrayID,
			'title'					:devAddress,
			'status'				:Status,
			'slot'					:Slot,
			'parentslot'			:ParentSlot,
			'relativeslot'			:RelativeSlot,
			'alarmcontrol'			:AlarmControl,
			'wwn'					:WWN,
			'drivetype'				:driveType,
			'faultsensed'			:FaultSensed,
			}))

	return {'enclosures':enclosures,
	   		'controllers':controllers,
	   		'batteries':batteries,
	   		'tempsensors':tempsensors,
	   		'scsiports':scsiports,
	   		'supportCRUs':supportCRUs,
	   		'drives':drives,
	   		}


# Return a dictionary structure for events
def getEvent(cmd,summary,message=None,clear=False):
    event = dict(
      summary=summary,
      component=cmd.component,
    )

    if message:
      event['message'] = message

    if clear:
      event['severity'] = 0
    else:
      event['severity'] = cmd.severity

    return event
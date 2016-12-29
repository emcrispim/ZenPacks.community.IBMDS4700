##########################################################################
# Author:               Eduardo Crispim, emcrispim@gmail.com
# Date:                 December, 2016
# 
# This program is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License version 2 or (at your
# option) any later version as published by the Free Software Foundation.
#
#########################################################################


from Products.DataCollector.plugins.CollectorPlugin import CommandPlugin
from Products.DataCollector.plugins.DataMaps import ObjectMap, RelationshipMap
import telnetlib
from  xml.dom.minidom import parseString
import re

class IBMDS4700(CommandPlugin):
	transport = "python"
	
	def collect(self,device,log):
		t = telnetlib.Telnet(  )
		t.open(device.manageIp)
		results = t.read_until(device.zTelnetLoginRegex,device.zCommandCommandTimeout)
		t.write(device.zCommandUsername+'\n')
		results = t.read_until(device.zTelnetPasswordRegex,device.zCommandCommandTimeout)
		t.write(device.zCommandPassword+'\n')
		results = t.read_until('-> ',device.zCommandCommandTimeout)
		t.write('ssmShowTree 2\n')
		results = t.read_until('-> ',device.zCommandCommandTimeout)
		return results

	def preprocess(self,results,log):

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

			elif len(findText(line,"devAddress:")):
				storage+= "\n<devAddress>%s</devAddress>" % line.split(':')[1].replace(" ","")
			elif len(findText(line,"devAddress:")):
				storage+= "\n<devAddress>%s</devAddress>" % line.split(':')[1].replace(" ","")
			elif len(findText(line,"  Status:")):
				storage+= "\n<Status>%s</Status>" % line.split(':')[1].replace(" ","")
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
				
		for i in range(len(tags)):
			storage+= "</%s>" % tags.pop()[0]

		#print storage
		xml = parseString(storage)
		return xml

	def process(self,device,results,log):
		xmlenclosures = results.getElementsByTagName('Enclosure')
		maps = []
		enclosures = []
		controllers = []
		supportCRUs = []
		alarms = []
		drives = []
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
					elif el.tagName == 'Controller':
						controllers.append(el)
					elif el.tagName == 'SupportCRU':
						supportCRUs.append(el)
					elif el.tagName == 'Alarm':
						alarms.append(el)
					elif el.tagName == 'Drive':
						drives.append(el)

				
			enclosures.append(ObjectMap(data={
				'id'			: self.prepId(devAddress),
				'status'		: Status,
				'slot'			: Slot,
				'parentslot'	: ParentSlot,
				'relativeslot'	: RelativeSlot,
				'alarmcontrol'	: AlarmControl,
				'failure'		: Failure,
				'warning'		: EWarning,
				}))
		
		maps.append(RelationshipMap(
			relname = 'enclosures',
			modname = 'Zenpacks.community.IBMDS4700.enclosures',
			objmaps = enclosures
			))
		import pdb;pdb.set_trace()
		return maps



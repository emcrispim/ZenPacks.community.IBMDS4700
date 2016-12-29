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
from Products.DataCollector.plugins.DataMaps import RelationshipMap
from ZenPacks.community.IBMDS4700 import Utils

class IBMDS4700(CommandPlugin):
	transport = "python"
	
	def collect(self,device,log):
		return Utils.telnetClient(
			device.zTelnetLoginRegex,
			device.p,
			device.zTelnetPasswordRegex,
			device.zCommandUsername,
			device.zCommandPassword,
			device.manageIp
			)

	def preprocess(self,results,log):
		return Utils.xmlencode(results)

	def process(self,device,results,log):

		data = Utils.processxml(results,self)
		maps = []		

		maps.append(RelationshipMap(
			relname = 'enclosure',
			modname = 'ZenPacks.community.IBMDS4700.Enclosure',
			objmaps = data['enclosures']
			))

		maps.append(RelationshipMap(
			relname = 'controller',
			modname = 'ZenPacks.community.IBMDS4700.Controller',
			objmaps = data['controllers']
			))

		maps.append(RelationshipMap(
			relname = 'battery',
			modname = 'ZenPacks.community.IBMDS4700.Battery',
			objmaps = data['batteries']
			))

		maps.append(RelationshipMap(
			relname = 'tempsensor',
			modname = 'ZenPacks.community.IBMDS4700.TempSensor',
			objmaps = data['tempsensors']
			))

		maps.append(RelationshipMap(
			relname = 'scsiport',
			modname = 'ZenPacks.community.IBMDS4700.SCSIPort',
			objmaps = data['scsiports']
			))

		maps.append(RelationshipMap(
			relname = 'powersupply',
			modname = 'ZenPacks.community.IBMDS4700.PowerSupply',
			objmaps = data['supportCRUs']
			))

		maps.append(RelationshipMap(
			relname = 'drive',
			modname = 'ZenPacks.community.IBMDS4700.Drive',
			objmaps = data['drives']
			))
		
		return maps



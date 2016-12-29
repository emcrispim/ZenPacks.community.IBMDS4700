
##########################################################################
# Author:               Eduardo Crispim, emcrispim@gmail.com
# Date:                 December, 2016
# 
# This program is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License version 2 or (at your
# option) any later version as published by the Free Software Foundation.
#
#########################################################################


productNames = (
	'IBMDS4700Device',
	'Enclosure',
	'Controller',
	'Battery',
	'TempSensor',
	'SCSIPort',
	'PowerSupply',
	'Drive'
	)

class ZenPack(ZenPackBase):

  def install(self, dmd):
    # create the required device class 
    dc = dmd.Devices.createOrganizer('/Storage/IBMDS4700')
    ZenPackBase.install(self, dmd)

  def remove(self, dmd, leaveObjects=False):
    
    if not leaveObjects:
      
      # Delete all instances of devices in /Storage/IBMDS4700 - completely - including history and events
      #
      for dev in dmd.Devices.Storage.IBMDS4700.getSubDevices():
        dev.deleteDevice(deleteStatus=True, deleteHistory=True, deletePerf=True)
         

      # Next line delete all subclasses too
      dmd.Devices.manage_deleteOrganizer('/Storage/IBMDS4700')

      ZenPackBase.remove(self, dmd, leaveObjects=leaveObjects)
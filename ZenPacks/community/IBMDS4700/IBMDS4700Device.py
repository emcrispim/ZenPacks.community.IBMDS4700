
##########################################################################
# Author:               Eduardo Crispim, emcrispim@gmail.com
# Date:                 December, 2016
# 
# This program is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License version 2 or (at your
# option) any later version as published by the Free Software Foundation.
#
#########################################################################


from Products.ZenModel.Device import Device
from Products.ZenRelations.RelSchema import ToManyCont, ToOne

class IBMDS4700Device(Device):
  
  
  meta_type = portal_type = 'IBMDS4700Device'
 

  storage_array = None
  
  _properties = Device._properties + (
  	{'id': 'storage_array','type':'string'},
  )
  
  _relations = Device._relations + (
    ('enclosure',ToManyCont(ToOne,'ZenPacks.community.IBMDS4700.Enclosure','enclosure_device',)),
    ('controller',ToManyCont(ToOne,'ZenPacks.community.IBMDS4700.Controller','controller_device',)),
    ('battery',ToManyCont(ToOne,'ZenPacks.community.IBMDS4700.Battery','battery_device',)),
    ('tempsensor',ToManyCont(ToOne,'ZenPacks.community.IBMDS4700.TempSensor','tempsensor_device',)),
    ('scsiport',ToManyCont(ToOne,'ZenPacks.community.IBMDS4700.SCSIPort','scsiport_device',)),
    ('powersupply',ToManyCont(ToOne,'ZenPacks.community.IBMDS4700.PowerSupply','powersupply_device',)),
    ('drive',ToManyCont(ToOne,'ZenPacks.community.IBMDS4700.Drive','drive_device',)),
  )
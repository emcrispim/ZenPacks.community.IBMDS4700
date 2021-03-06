##########################################################################
# Author:               Eduardo Crispim, emcrispim@gmail.com
# Date:                 December, 2016
# 
# This program is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License version 2 or (at your
# option) any later version as published by the Free Software Foundation.
#
#########################################################################

from Products.ZenModel.DeviceComponent import DeviceComponent
from Products.ZenModel.ManagedEntity import ManagedEntity
from Products.ZenModel.ZenossSecurity import ZEN_CHANGE_DEVICE
from Products.ZenRelations.RelSchema import ToManyCont, ToOne

class TempSensor(DeviceComponent,ManagedEntity):
  meta_type = portal_type = "IBMDS4700TempSensor"

  status = None
  slot = None
  parentslot = None
  relativeslot = None
  alarmcontrol = None


  

  _properties = ManagedEntity._properties + (
    {'id': 'status', 'type': 'string'},
    {'id': 'slot', 'type': 'int'},
    {'id': 'parentslot', 'type': 'int'},
    {'id': 'relativeslot', 'type': 'int'},
    {'id': 'alarmcontrol', 'type': 'string'},
  )

  _relations = ManagedEntity._relations + (
    ('tempsensor_device', ToOne(ToManyCont,
      'ZenPacks.community.IBMDS4700.IBMDS4700Device','tempsensor',
      ),
    ),
  )


  factory_type_information = ({
    'actions': ({
      'id': 'perfConf',
      'name': 'Template',
      'action': 'objTemplates',
      'permissions': (ZEN_CHANGE_DEVICE,),
    },),
  },)

  def device(self):
    return self.tempsensor_device()

  def getRRDTemplateName(self):
    return 'IBMDS4700TempSensor'
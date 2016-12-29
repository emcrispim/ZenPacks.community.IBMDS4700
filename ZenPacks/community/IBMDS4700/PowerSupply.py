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

class PowerSupply(DeviceComponent,ManagedEntity):
  meta_type = portal_type = "IBMDS4700PowerSupply"

  status = None
  slot = None
  parentslot = None
  relativeslot = None
  alarmcontrol = None
  sn = None
  pn = None
  alarmcontrol = None
  fanstatus = None
  powersupplystatus = None
  haspowerinput = None
  tempsensorstatus = None
  temperature = None
  

  _properties = ManagedEntity._properties + (
    {'id': 'status', 'type': 'string'},
    {'id': 'slot', 'type': 'int'},
    {'id': 'parentslot', 'type': 'int'},
    {'id': 'relativeslot', 'type': 'int'},
    {'id': 'sn', 'type': 'string'},
    {'id': 'pn', 'type': 'string'},
    {'id': 'alarmcontrol', 'type': 'string'},
    {'id': 'fanstatus', 'type': 'string'},
    {'id': 'powersupplystatus', 'type': 'string'},
    {'id': 'haspowerinput', 'type': 'string'},
    {'id': 'tempsensorstatus', 'type': 'string'},
    {'id': 'temperature', 'type': 'string'},

    

  )

  _relations = ManagedEntity._relations + (
    ('powersupply_device', ToOne(ToManyCont,
      'ZenPacks.community.IBMDS4700.IBMDS4700Device','powersupply',
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
    return self.powersupply_device()

  def getRRDTemplateName(self):
    return 'IBMDS4700PowerSupply'
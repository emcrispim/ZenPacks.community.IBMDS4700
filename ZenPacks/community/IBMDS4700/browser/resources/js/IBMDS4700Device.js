//#######################################################################
// Author:               Eduardo Crispim, emcrispim@gmail.com
// Date:                 September, 2016
// 
// This program is free software; you can redistribute it and/or modify it
// under the terms of the GNU General Public License version 2 or (at your
// option) any later version as published by the Free Software Foundation.
//

(function(){
  var ZC = Ext.ns('Zenoss.component');

  ZC.registerName(
    'IBMDS4700Enclosure',
    _t('Enclosure'),
    _t('Enclosures')
  );

  ZC.registerName(
    'IBMDS4700Controller',
    _t('Controller'),
    _t('Controllers')
  );

  ZC.registerName(
    'IBMDS4700Battery',
    _t('Battery'),
    _t('Batteries')
  );

   ZC.registerName(
    'IBMDS4700TempSensor',
    _t('Temp Sensor'),
    _t('Temp Sensors')
  );

  ZC.registerName(
    'IBMDS4700SCSIPort',
    _t('SCSI Port'),
    _t('SCSI Ports')
  );

  ZC.registerName(
    'IBMDS4700PowerSupply',
    _t('Power Supply'),
    _t('Power Supplies')
  );

   ZC.registerName(
    'IBMDS4700Drive',
    _t('Drive'),
    _t('Drives')
  );

   ZC.IBMDS4700EnclosurePanel = Ext.extend(ZC.ComponentGridPanel,{
    constructor: function(config){
      config = Ext.applyIf(config||{}, {
        componentType: 'IBMDS4700Enclosure',
        autoExpandColumn: 'name',
        sortInfo: {
          field: 'name',
          direction: 'DESC'
        },
        fields: [
          {name: 'uid'},
          {name: 'name'},
          {name: 'controllerenclosure'},
          {name: 'status'},
          {name: 'severity'},
          {name: 'slot',type:'int'},
          {name: 'parentslot',type:'int'},
          {name: 'relativeslot',type:'int'},
          {name: 'alarmcontrol'},
          {name: 'failure'},
          {name: 'warning'},
          {name: 'sn'},
          {name: 'pn'}
        ],
        columns: [
          {
            id: 'severity',
            dataIndex: 'severity',
            header: _t('Events'),
            renderer: Zenoss.render.severity,
            sortable: true,
            width: 50
          },{
            id: 'name',
            dataIndex: 'name',
            header: _t('Enclosure ID'),
            sortable: true
          },{
            id: 'status',
            dataIndex: 'status',
            header: _t('Status'),
            sortable: true,
            width:70
          },{
            id: 'controllerenclosure',
            dataIndex: 'controllerenclosure',
            header: _t('Controller Enclosure'),
            sortable: true,
            width:120
          },{  
            id: 'slot',
            dataIndex: 'slot',
            header: _t('Slot'),
            sortable: true,
            width:70
          },{  
            id: 'parentslot',
            dataIndex: 'parentslot',
            header: _t('Parent Slot'),
            sortable: true,
            width:70
          },{
            id: 'relativeslot',
            dataIndex: 'relativeslot',
            header: _t('Relative Slot'),
            sortable: true,
            width:90
          },{
            id: 'alarmcontrol',
            dataIndex: 'alarmcontrol',
            header: _t('Alarm Control'),
            sortable: true,
            width:90
          },{
            id: 'failure',
            dataIndex: 'failure',
            header: _t('Failure'),
            sortable: true,
            width:70
          },{
            id: 'warning',
            dataIndex: 'warning',
            header: _t('Warning'),
            sortable: true,
            width:100
          },{
            id: 'sn',
            dataIndex: 'sn',
            header: _t('SN'),
            sortable: true,
            width:100
          },{
            id: 'pn',
            dataIndex: 'pn',
            header: _t('PN'),
            sortable: true,
            width:100
          }
        ]
      });

      ZC.IBMDS4700EnclosurePanel.superclass.constructor.call(this,config);
    }
  });


  ZC.IBMDS4700ControllerPanel = Ext.extend(ZC.ComponentGridPanel,{
    constructor: function(config){
      config = Ext.applyIf(config||{}, {
        componentType: 'IBMDS4700Controller',
        autoExpandColumn: 'name',
        sortInfo: {
          field: 'name',
          direction: 'DESC'
        },
        fields: [
          {name: 'uid'},
          {name: 'name'},
          {name: 'status'},
          {name: 'severity'},
          {name: 'ctype'},
          {name: 'slot',type:'int'},
          {name: 'parentslot',type:'int'},
          {name: 'relativeslot',type:'int'},
          {name: 'sn'},
          {name: 'pn'},
          {name: 'alarmcontrol'},
          {name: 'enclosureid'}
        ],
        columns: [
          {
            id: 'severity',
            dataIndex: 'severity',
            header: _t('Events'),
            renderer: Zenoss.render.severity,
            sortable: true,
            width: 50
          },{
            id: 'name',
            dataIndex: 'name',
            header: _t('Enclosure ID'),
            sortable: true
          },{
            id: 'status',
            dataIndex: 'status',
            header: _t('Status'),
            sortable: true,
            width:70
          },{
            id: 'ctype',
            dataIndex: 'ctype',
            header: _t('Type'),
            sortable: true,
            width:70
          },{  
            id: 'slot',
            dataIndex: 'slot',
            header: _t('Slot'),
            sortable: true,
            width:70
          },{  
            id: 'parentslot',
            dataIndex: 'parentslot',
            header: _t('Parent Slot'),
            sortable: true,
            width:70
          },{
            id: 'relativeslot',
            dataIndex: 'relativeslot',
            header: _t('Relative Slot'),
            sortable: true,
            width:90
          },{
            id: 'sn',
            dataIndex: 'sn',
            header: _t('SN'),
            sortable: true,
            width:100
          },{
            id: 'pn',
            dataIndex: 'pn',
            header: _t('PN'),
            sortable: true,
            width:100
          },{
            id: 'alarmcontrol',
            dataIndex: 'alarmcontrol',
            header: _t('Alarm Control'),
            sortable: true,
            width:90
          },{
            id: 'enclosureid',
            dataIndex: 'enclosureid',
            header: _t('Enclosure ID'),
            sortable: true,
            width:90
          }
        ]
      });

      ZC.IBMDS4700ControllerPanel.superclass.constructor.call(this,config);
    }
  });


  ZC.IBMDS4700BatteryPanel = Ext.extend(ZC.ComponentGridPanel,{
    constructor: function(config){
      config = Ext.applyIf(config||{}, {
        componentType: 'IBMDS4700Battery',
        autoExpandColumn: 'name',
        sortInfo: {
          field: 'name',
          direction: 'DESC'
        },
        fields: [
          {name: 'uid'},
          {name: 'name'},
          {name: 'status'},
          {name: 'severity'},
          {name: 'slot',type:'int'},
          {name: 'parentslot',type:'int'},
          {name: 'relativeslot',type:'int'},
          {name: 'sn'},
          {name: 'pn'},
          {name: 'alarmcontrol'},
          {name: 'installationtime'},
          {name: 'expirationtime'}
        ],
        columns: [
          {
            id: 'severity',
            dataIndex: 'severity',
            header: _t('Events'),
            renderer: Zenoss.render.severity,
            sortable: true,
            width: 50
          },{
            id: 'name',
            dataIndex: 'name',
            header: _t('Enclosure ID'),
            sortable: true
          },{
            id: 'status',
            dataIndex: 'status',
            header: _t('Status'),
            sortable: true,
            width:70
          },{  
            id: 'slot',
            dataIndex: 'slot',
            header: _t('Slot'),
            sortable: true,
            width:70
          },{  
            id: 'parentslot',
            dataIndex: 'parentslot',
            header: _t('Parent Slot'),
            sortable: true,
            width:70
          },{
            id: 'relativeslot',
            dataIndex: 'relativeslot',
            header: _t('Relative Slot'),
            sortable: true,
            width:90
          },{
            id: 'sn',
            dataIndex: 'sn',
            header: _t('SN'),
            sortable: true,
            width:100
          },{
            id: 'pn',
            dataIndex: 'pn',
            header: _t('PN'),
            sortable: true,
            width:100
          },{
            id: 'alarmcontrol',
            dataIndex: 'alarmcontrol',
            header: _t('Alarm Control'),
            sortable: true,
            width:90
           },{
            id: 'installationtime',
            dataIndex: 'installationtime',
            header: _t('Installation Time'),
            sortable: true,
            width:120
           },{
            id: 'expirationtime',
            dataIndex: 'expirationtime',
            header: _t('Expiration Time'),
            sortable: true,
            width:120
          }
        ]
      });

      ZC.IBMDS4700BatteryPanel.superclass.constructor.call(this,config);
    }
  });

    ZC.IBMDS4700TempSensorPanel = Ext.extend(ZC.ComponentGridPanel,{
    constructor: function(config){
      config = Ext.applyIf(config||{}, {
        componentType: 'IBMDS4700TempSensor',
        autoExpandColumn: 'name',
        sortInfo: {
          field: 'name',
          direction: 'DESC'
        },
        fields: [
          {name: 'uid'},
          {name: 'name'},
          {name: 'severity'},
          {name: 'status'},
          {name: 'slot',type:'int'},
          {name: 'parentslot',type:'int'},
          {name: 'relativeslot',type:'int'},
          {name: 'alarmcontrol'}
        ],
        columns: [
          {
            id: 'severity',
            dataIndex: 'severity',
            header: _t('Events'),
            renderer: Zenoss.render.severity,
            sortable: true,
            width: 50
          },{
            id: 'name',
            dataIndex: 'name',
            header: _t('Enclosure ID'),
            sortable: true
          },{
            id: 'status',
            dataIndex: 'status',
            header: _t('Status'),
            sortable: true,
            width:70
          },{  
            id: 'slot',
            dataIndex: 'slot',
            header: _t('Slot'),
            sortable: true,
            width:70
          },{  
            id: 'parentslot',
            dataIndex: 'parentslot',
            header: _t('Parent Slot'),
            sortable: true,
            width:70
          },{
            id: 'relativeslot',
            dataIndex: 'relativeslot',
            header: _t('Relative Slot'),
            sortable: true,
            width:90
          },{
            id: 'alarmcontrol',
            dataIndex: 'alarmcontrol',
            header: _t('Alarm Control'),
            sortable: true,
            width:90
          }
        ]
      });

      ZC.IBMDS4700TempSensorPanel.superclass.constructor.call(this,config);
    }
  });


 ZC.IBMDS4700SCSIPortPanel = Ext.extend(ZC.ComponentGridPanel,{
    constructor: function(config){
      config = Ext.applyIf(config||{}, {
        componentType: 'IBMDS4700SCSIPort',
        autoExpandColumn: 'name',
        sortInfo: {
          field: 'name',
          direction: 'DESC'
        },
        fields: [
          {name: 'uid'},
          {name: 'name'},
          {name: 'status'},
          {name: 'severity'},
          {name: 'slot',type:'int'},
          {name: 'parentslot',type:'int'},
          {name: 'relativeslot',type:'int'},
          {name: 'alarmcontrol'},
          {name: 'lostlink'},
          {name: 'transmitfailed'}

        ],
        columns: [
          {
            id: 'severity',
            dataIndex: 'severity',
            header: _t('Events'),
            renderer: Zenoss.render.severity,
            sortable: true,
            width: 50
          },{
            id: 'name',
            dataIndex: 'name',
            header: _t('Enclosure ID'),
            sortable: true
          },{
            id: 'status',
            dataIndex: 'status',
            header: _t('Status'),
            sortable: true,
            width:70
          },{  
            id: 'slot',
            dataIndex: 'slot',
            header: _t('Slot'),
            sortable: true,
            width:70
          },{  
            id: 'parentslot',
            dataIndex: 'parentslot',
            header: _t('Parent Slot'),
            sortable: true,
            width:70
          },{
            id: 'relativeslot',
            dataIndex: 'relativeslot',
            header: _t('Relative Slot'),
            sortable: true,
            width:90
          },{
            id: 'alarmcontrol',
            dataIndex: 'alarmcontrol',
            header: _t('Alarm Control'),
            sortable: true,
            width:90
          },{
            id: 'lostlink',
            dataIndex: 'lostlink',
            header: _t('Lost Link'),
            sortable: true,
            width:90
          },{
            id: 'transmitfailed',
            dataIndex: 'transmitfailed',
            header: _t('Transmit Failed'),
            sortable: true,
            width:90
          }
        ]
      });

      ZC.IBMDS4700SCSIPortPanel.superclass.constructor.call(this,config);
    }
  });

ZC.IBMDS4700PowerSupplyPanel = Ext.extend(ZC.ComponentGridPanel,{
    constructor: function(config){
      config = Ext.applyIf(config||{}, {
        componentType: 'IBMDS4700PowerSupply',
        autoExpandColumn: 'name',
        sortInfo: {
          field: 'name',
          direction: 'DESC'
        },
        fields: [
          {name: 'uid'},
          {name: 'name'},
          {name: 'status'},
          {name: 'severity'},
          {name: 'slot',type:'int'},
          {name: 'parentslot',type:'int'},
          {name: 'relativeslot',type:'int'},
          {name: 'alarmcontrol'},
          {name: 'sn'},
          {name: 'pn'},
          {name: 'fanstatus'},
          {name: 'powersupplystatus'},
          {name: 'haspowerinput'},
          {name: 'tempsensorstatus'},
          {name: 'temperature'}
        
        ],
        columns: [
          {
            id: 'severity',
            dataIndex: 'severity',
            header: _t('Events'),
            renderer: Zenoss.render.severity,
            sortable: true,
            width: 50
          },{
            id: 'name',
            dataIndex: 'name',
            header: _t('ID'),
            sortable: true
          },{
            id: 'status',
            dataIndex: 'status',
            header: _t('Status'),
            sortable: true,
            width:60
          },{  
            id: 'slot',
            dataIndex: 'slot',
            header: _t('Slot'),
            sortable: true,
            width:50
          },{  
            id: 'parentslot',
            dataIndex: 'parentslot',
            header: _t('Parent Slot'),
            sortable: true,
            width:70
          },{
            id: 'relativeslot',
            dataIndex: 'relativeslot',
            header: _t('Relative Slot'),
            sortable: true,
            width:90
          },{
            id: 'alarmcontrol',
            dataIndex: 'alarmcontrol',
            header: _t('Alarm Control'),
            sortable: true,
            width:90
          },{
            id: 'sn',
            dataIndex: 'sn',
            header: _t('SN'),
            sortable: true,
            width:90
          },{
            id: 'pn',
            dataIndex: 'pn',
            header: _t('PN'),
            sortable: true,
            width:60
          },{
            id: 'fanstatus',
            dataIndex: 'fanstatus',
            header: _t('Fan Status'),
            sortable: true,
            width:90
          },{
            id: 'powersupplystatus',
            dataIndex: 'powersupplystatus',
            header: _t('Power Supply Status'),
            sortable: true,
            width:120
          },{
            id: 'haspowerinput',
            dataIndex: 'haspowerinput',
            header: _t('Has Power Input?'),
            sortable: true,
            width:120
          },{
            id: 'tempsensorstatus',
            dataIndex: 'tempsensorstatus',
            header: _t('Temperature Status'),
            sortable: true,
            width:120
          },{
            id: 'temperature',
            dataIndex: 'temperature',
            header: _t('Temperature (C)'),
            sortable: true,
            width:90
          }
        ]
      });

      ZC.IBMDS4700PowerSupplyPanel.superclass.constructor.call(this,config);
    }
  });


ZC.IBMDS4700DrivePanel = Ext.extend(ZC.ComponentGridPanel,{
    constructor: function(config){
      config = Ext.applyIf(config||{}, {
        componentType: 'IBMDS4700Drive',
        autoExpandColumn: 'name',
        sortInfo: {
          field: 'name',
          direction: 'DESC'
        },
        fields: [
          {name: 'uid'},
          {name: 'name'},
          {name: 'status'},
          {name: 'severity'},
          {name: 'slot',type:'int'},
          {name: 'parentslot',type:'int'},
          {name: 'relativeslot',type:'int'},
          {name: 'alarmcontrol'},
          {name: 'wwn'},
          {name: 'drivetype'},
          {name: 'faultsensed'},
          {name: 'trayid'}
        
        ],
        columns: [
          {
            id: 'severity',
            dataIndex: 'severity',
            header: _t('Events'),
            renderer: Zenoss.render.severity,
            sortable: true,
            width: 50
          },{
            id: 'name',
            dataIndex: 'name',
            header: _t('ID'),
            sortable: true
          },{
            id: 'status',
            dataIndex: 'status',
            header: _t('Status'),
            sortable: true,
            width:60
          },{  
            id: 'slot',
            dataIndex: 'slot',
            header: _t('Slot'),
            sortable: true,
            width:50
          },{  
            id: 'parentslot',
            dataIndex: 'parentslot',
            header: _t('Parent Slot'),
            sortable: true,
            width:70
          },{
            id: 'relativeslot',
            dataIndex: 'relativeslot',
            header: _t('Relative Slot'),
            sortable: true,
            width:90
          },{
            id: 'alarmcontrol',
            dataIndex: 'alarmcontrol',
            header: _t('Alarm Control'),
            sortable: true,
            width:90
          },{
            id: 'wwn',
            dataIndex: 'wwn',
            header: _t('WWN'),
            sortable: true,
            width:140
          },{
            id: 'drivetype',
            dataIndex: 'drivetype',
            header: _t('Drive Type'),
            sortable: true,
            width:90
          },{
            id: 'faultsensed',
            dataIndex: 'faultsensed',
            header: _t('Fault Sensed?'),
            sortable: true,
            width:90
          },{
            id: 'trayid',
            dataIndex: 'trayid',
            header: _t('Enclosure ID'),
            sortable: true,
            width:90
          }
        ]
      });

      ZC.IBMDS4700DrivePanel.superclass.constructor.call(this,config);
    }
  });


  Ext.reg('IBMDS4700EnclosurePanel',ZC.IBMDS4700EnclosurePanel);
  Ext.reg('IBMDS4700ControllerPanel',ZC.IBMDS4700ControllerPanel);
  Ext.reg('IBMDS4700BatteryPanel',ZC.IBMDS4700BatteryPanel);
  Ext.reg('IBMDS4700TempSensorPanel',ZC.IBMDS4700TempSensorPanel);
  Ext.reg('IBMDS4700SCSIPortPanel',ZC.IBMDS4700SCSIPortPanel);
  Ext.reg('IBMDS4700PowerSupplyPanel',ZC.IBMDS4700PowerSupplyPanel);
  Ext.reg('IBMDS4700DrivePanel',ZC.IBMDS4700DrivePanel);


  })(); 
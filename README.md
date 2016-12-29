================================
ZenPacks.community.IBMDS4700
================================


About
=====

This project is a extension (ZenPack) for the Zenoss, it models and monitors the
IBM DS4700 through telnet


Requirements
============

Zenoss
------

You must first have, or install, Zenoss 4.2 or later. This ZenPack was tested
against Zenoss 4.2 only

Installation

============


Normal Installation (packaged egg)
----------------------------------

Download the IBMDS4700 ZenPack egg file
Copy this file to your Zenoss server and run the following commands as the zenoss
user.


        zenpack --install ZenPacks.community.IBMDS4700.egg
        zenoss restart

Developer Installation (link mode)
----------------------------------

If you wish to further develop and possibly contribute back to the IBMV7000
ZenPack you should clone the git [https://github.com/emcrispim/ZenPacks.community.IBMDS4700](https://github.com/emcrispim/ZenPacks.community.IBMDS4700),
then install the ZenPack in developer mode using the following commands.


        git clone git://github.com/emcrispim/ZenPacks.community.IBMDS4700.git
        zenpack --link --install ZenPacks.community.IBMV7000
        zenoss restart

After Installation
-------------------

The IBMDS4700 ZenPack will create a new device class organizer "/Storage/DS4700". 

Usage
=====

You have to set the following configurarion properties

Configuration Properties
------------------------
- zCommandUsername
- zCommandPassword
- zTelnetLoginRegex
- zTelnetPasswordRegex

The zCommandUsername it's the telnet user usually is "shellUsr" and the zCommandPassword the telnet password.
The zTelnetLoginRegex it's the login prompt put this in the property value "login: " and zTelnetPasswordRegex must be "password: ". 

This Zenpack models the:
- Enclosures
- Controllers
- Power Supplies
- Drives
- SCSI Ports
- Batteries
- Temperature Sensor





#!/usr/bin/python
#
# Disconnect all active pidgin accounts on suspend and reconnect all
# active pidgin accounts on resume.
#
# Place in /etc/pm/sleep.d/
#
# Name should start with a low number e.g. "05_pidginsuspend" and you
# have to set the execute bit (i.e. sudo chmod +x)
#
# Author: Joshua A Haas

import dbus,sys,syslog

def sleep(purple):
  
  accounts = purple.PurpleAccountsGetAllActive()
  for a in accounts:
    purple.PurpleAccountDisconnect(a)

def wake(purple):
  
  accounts = purple.PurpleAccountsGetAllActive()
  for a in accounts:
    purple.PurpleAccountConnect(a)

def main():
  
  bus = dbus.SessionBus()
  obj = bus.get_object("im.pidgin.purple.PurpleService", "/im/pidgin/purple/PurpleObject")
  purple = dbus.Interface(obj, "im.pidgin.purple.PurpleInterface")
  
  if len(sys.argv)<2:
    syslog.syslog('Must be called with "suspend" or "resume" as parameter')
    sys.exit(1)
  
  if sys.argv[1]=='suspend':
    sleep(purple)
  elif sys.argv[1]=='resume':
    wake(purple)
  else:
    syslog.syslog('Invalid parameter: "'+sys.argv[1]+'"')
    sys.exit(2)

if __name__=='__main__':
  main()

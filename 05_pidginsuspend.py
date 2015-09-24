#!/usr/bin/python

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

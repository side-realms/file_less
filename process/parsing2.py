import os.path
import argparse
import xml.etree.ElementTree as ET
import re
import obfuscation/dictionary as di

# Windows Command to generate the XML file
# wevtutil query-events "Windows Powershell" /uni:true /f:XML > winps.xml

parser=argparse.ArgumentParser(description='A parser for the Windows Powershell event log XML generated by wevutil command.')
parser.add_argument('xml', help='Path of the XML File')
args=parser.parse_args()
filename=args.xml
if not os.path.isfile(filename):
  print('Not found:%s' % filename)
  exit(1)
ns='{http://schemas.microsoft.com/win/2004/08/events/event}'  #namespace
comment_out = r'^\s*(#.*|)$'
Invoke = r'Invoke-WebEwquest'
f = open(filename, 'r', encoding='utf-16')
xml=f.read()
#print(xml)
xml= "<eventlog>" + xml + "</eventlog>"
root = ET.fromstring(xml)
alert_command = '(Get-Host).UI.RawUI.ForegroundColor = \'red\''
reposit_command = '(Get-Host).UI.RawUI.ForegroundColor = \'white\''
for event in root:
  for e in event:
    for f in e:
      pass
  eventid=event.find(ns + 'System').find(ns + 'EventID').text
  eventrecid=event.find(ns + 'System').find(ns + 'EventRecordID').text
  time=event.find(ns + 'System').find(ns + 'TimeCreated').attrib
  ps=event.find(ns + 'EventData').findall(ns + 'Data')
  if eventid=="4104":
    if(ps[0].text):
      split = ps[0].text.splitlines()
      print(split)
      for column in split:
          di.check(column)

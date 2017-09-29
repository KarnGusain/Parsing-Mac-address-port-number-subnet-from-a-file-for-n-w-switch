#!/usr/bin/env python
with open('test', 'r') as mailfile:
  for line in mailfile:
    if line.startswith('Sep') :
      startBlock  = line.find('<')
      if startBlock >= 0:
       endBlock = line.find('>, ',startBlock)
       host = line[ startBlock+1 : endBlock ]
       mailAddress = host.replace(">,<"," ")
       print(mailAddress)

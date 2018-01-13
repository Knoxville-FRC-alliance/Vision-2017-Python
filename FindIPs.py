#!/usr/bin/python

#######
####### This code is to run automatically when the Pi is turned on, and will find the IP the rio is on and put it in a text document to be read by the main vision file
#######

import time
import os
import subprocess as sp
import re
import sys
import select
from subprocess import call

RioMacAddress = ['00:80:2F:25:B2:2F', '00:80:2F:17:F9:1A'] #Put the Rio's MAC Address here, the first MAC Address is the Rio currently on the Kiwibot
#RioMacAddress.append('58:E2:8F:40:DD:3D') # MAC address of iPhone for testing
RioMacAddress.append('78:4F:43:91:8D:F9') # Computer MAC address

regex = ur"(\d+[.]\d+[.]\d+[.]\d+).*?(\w\w:\w\w:\w\w:\w\w:\w\w:\w\w)" #Used to pull the IPs and MAC Addresses from the console
netMask = ur"[0-9]{1,3}[.][0-9]{1,3}[.][0-9]{1,3}[.]" #Used to find the subnet mask
loopLimit = 10000

hostNameFound = False

while True:
        try:
                loopLimit = loopLimit - 1
                if loopLimit < 0:
                        print("FindIP - Loop limit reached")
                        break
                myIP = sp.check_output("hostname -I", shell=True) #Gets my IP
                if not (myIP and not myIP.strip()):
                        hostNameFound = True
                        break
                if QKeyWasPressed() == True:
                        print("FindIP - Breaking....")
                        break
		print("FindIP - Retrying IP (Try)")
                time.sleep(1)
        except KeyboardInterrupt:
                print("FindIP - Breaking...")
                break
        except:
                print("FindIP - Retrying IP (Except)")
                time.sleep(1)

if (hostNameFound == False):
        print("FindIP - Cancelled")
        sys.exit(0)

        
print("FindIP - {ip}".format(ip=myIP))
netMaskIP = re.findall(netMask, myIP) #Finds the subnet Mask
print("FindIP - Finding devices on subnet mask {ip}".format(ip=netMaskIP[0]))

rioIP = ''
macAddressCorrect = False 

def QKeyWasPressed():
        i,o,e = select.select([sys.stdin],[],[],0.0001)
        for s in i:
                if s == sys.stdin:
                        input = sys.stdin.readline()
                        print("FindIP - Input {inp}".format(inp=input))
                        if input == "q":
                                return True
                        return False
        return False

def Connect():
        global regex, netMask, myIP, netMaskIP, macAddressCorrect, rioIP
        macAddresses = sp.check_output("sudo nmap -sn {netmask}0/24".format(netmask=netMaskIP[0]), shell=True) #Searches all devices on the network for MacAddress and IPs
        parsedMacAddress = re.findall(regex, macAddresses, re.DOTALL) #Sorts out the MacAddresses
        print("FindIP - {pIP} Mac Addresses have been found".format(pIP=len(parsedMacAddress)))

        for thisMac in parsedMacAddress:
                if thisMac[1] in RioMacAddress:
                        rioIP = thisMac[0]
                        print("FindIP - Rio Connected, Local IP is {ip}".format(ip=rioIP))
                        macAddressCorrect = True
                        break

while macAddressCorrect == False:
        loopLimit = loopLimit - 1
        if loopLimit < 0:
                print("FindIP - Loop limit reached")
                break
        try:
                if QKeyWasPressed() == True:
                        print("FindIP - Breaking....")
                        break
                Connect()                
                if (macAddressCorrect == False): #This is hear just to keep this message from displaying the first time the code is run
                        print("FindIP - Failed MAC Address Validation, trying again ({pid})".format(pid=os.getpid()))
                #if keyboard.is_pressed('q'):
                #        print("Breaking....")
                #        break
        except KeyboardInterrupt:
                print("FindIP - Breaking...")
                break

if (macAddressCorrect == True):
        IPFile = open("/home/pi/git/Vision/Vision-2017-Python/ipdoc.txt", "w") #Opens the text document that the vision code will read for the IP
        IPFile.write(rioIP) #Writes the IP into the document
        IPFile.close()
        print("FindIP - Done Connecting")
else:
        print("FindIP - Cancelled")

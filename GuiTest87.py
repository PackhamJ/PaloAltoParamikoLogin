#This is a test gui application that is designed to call many other functions
#By calling other methods this app will ssh into a Palo Alto Firewall(May work on other boxes) run a command and pull information from the command that was run
#@author Jordan Packham viry2kphone@gmail.com
#version .000002 (This is the current version)
#Since    .000001 (Version number that this method was added to the PaloAltoParamikoLogin class)
#@param arrayValue will read and store the contents of file.txt
#@param findSomething will be used to search for this string in some of the received input from other methods
#@param command this value will be sent to sshOutput and is a command that will be sent to the device that sshOutput logs into.
#@param valueFound This is the information we received from the method findString we will output this to the file output.txt

from Tkinter import *
import SSH
import paramiko
import time
import ReadFile
import Find
import WriteOutput



arrayValue = ReadFile.openFile("file.txt")
command = 'show system info\n'
findSomething = 'sw-version'

def findSWVersion():
	findSomething = 'sw-version'
	
	
	
def findModel():
	findSomething = 'model'
	
	
def findSerialNumber():
	findSomething = 'serial'
	

def runScript():	
	for x in arrayValue:
		x = x.replace("\n","")
		print x
		sshOutput = SSH.connectToDevice(x, command)
		valueFound = Find.findString(findSomething, sshOutput)
		WriteOutput.appendOutput(valueFound, x, 'output.txt')
	
	
root = Tk()
button_1 = Button(root, text="Find Software Version", command=findSWVersion)
button_1.grid(row=1, column=0)

button_2 = Button(root, text="Find Model", command=findModel)
button_2.grid(row=2, column=0)

button_3 = Button(root, text="Find Serial Number", command=findSerialNumber)
button_3.grid(row=3, column=0)


button_4 = Button(root, text="Run Script", command=runScript)
button_4.grid(row=4, column=0)



root.mainloop()
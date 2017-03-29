#This is the main method application that is designed to call many other functions
#By calling other methods this app will ssh into a Palo Alto Firewall(May work on other boxes) run a command and pull information from the command that was run
#@author Jordan Packham viry2kphone@gmail.com
#version .082 (This is the current version)
#Since    .000001 (Version number that this method was added to the PaloAltoParamikoLogin class)
#@param arrayValue will read and store the contents of file.txt
#@param findSomething will be used to search for this string in some of the received input from other methods
#@param command this value will be sent to sshOutput and is a command that will be sent to the device that sshOutput logs into.
#@param valueFound This is the information we received from the method findString we will output this to the file output.txt


import SSH
import paramiko
import time
import ReadFile
import Find
import WriteOutput

arrayValue = ReadFile.openFile("file.txt")
findSomething = 'serial'
command = 'show system info\n'
#print arrayValue

for x in arrayValue:
			x = x.replace("\n","")
			print x
			sshOutput = SSH.connectToDevice(x, command)
			valueFound = Find.findString(findSomething, sshOutput)
			WriteOutput.appendOutput(valueFound, x, 'output.txt')
			
			

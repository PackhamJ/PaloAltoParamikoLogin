#@author Jordan Packham viry2kphone@gmail.com
#version .082 (This is the current version)
#Since    .000001 (Version number that this method was added to the PaloAltoParamikoLogin class)
#This method is made to SSH into a firewall input some show command and output the info to console as well as return the value of the output.
#@param ip this argument should be an IP address that the host PC running the python code can access
#@param sshCommand this is the command that you want to grab information from ie show system info
#This program uses paramiko and time imports from the python library.

import paramiko
import time


def connectToDevice(ip, sshCommand):
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	

	try:
		ssh.connect(ip, username='redacted',password='redacted', timeout=10)
		time.sleep(.25)
		channel = ssh.invoke_shell()
		output = channel.recv(10000)
		print output
		print "connected to device"
		
		
		channel.send(sshCommand)
		output3 = channel.recv(1000000)
		print output3
		
		time.sleep(10)
		channel.send('q')
		time.sleep(1)
		channel.send('\n')
		time.sleep(.5)
		channel.send('exit\n')
		time.sleep(.5)
		output2 = channel.recv(10000)
		#print output2
		time.sleep(10)
		return output2
		
		
		
		
	except:
		   # ssh.close() #just in case it connects, but does not finish the code in the try block
			print "did not connect to %s" % ip
			return 'failed'
     

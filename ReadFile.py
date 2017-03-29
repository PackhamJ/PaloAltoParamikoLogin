#This method opens a file as read only and puts the values into an array and returns the array values
#@author Jordan Packham viry2k@gmail.com
#version .082 (This is the current version)
#Since    .000001 (Version number that this method was added to the PaloAltoParamikoLogin class)
#@param fileName the name of the file that this method will read through.
#@return this method will return an array of the ip's that are in the file.




def openFile(fileName):
	with open(fileName, 'r') as ins:
		ipArray = []
		for line in ins:
			ipArray.append(line)
	#print ipArray
	return ipArray
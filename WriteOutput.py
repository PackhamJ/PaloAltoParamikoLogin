#@author Jordan Packham viry2k@gmail.com
#version .082 (This is the current version)
#Since    .000001 (Version number that this method was added to the PaloAltoParamikoLogin class)
#@param output: First output that you want to put into the file
#@param ip: 2nd output you want to put into the file IP + output will be concatenated with some spaces concatenated in between
#@param filename: the name of the file that you want to append to
#@return this method will return the string "Wrote line to file"

def appendOutput(output, ip, filename):
	target = open(filename, 'a')
	target.write( ip + ', ' + output)
	target.write("\n")
	#print (output + '     ' + ip)
	target.close()
	return 'Wrote line to file'
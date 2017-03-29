#This method takes two inputs and searches for a string and returns the entire line that contains that string
#@author Jordan Packham viry2k@gmail.com
#version .082 (This is the current version)
#Since    .000001 (Version number that this method was added to the PaloAltoParamikoLogin class)
#@param findWhat: This is the parameter that it will be looking for
#@param input: This is the data that the method will search through
#@return returnValue this is the line that contains the input that was found it is returned in a string value


def findString(findWhat, input):
	matched_lines = [line for line in input.split('\n') if findWhat in line]
	returnValue = ''.join(matched_lines)
	returnValue = returnValue.replace("\n","")
	returnValue = returnValue.replace("\r","")
	#print returnValue
	return returnValue
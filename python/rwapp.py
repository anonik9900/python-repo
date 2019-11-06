#!/usr/bin/python

#Open file
file = open("passwordlist","r")

#Loop through file until we find elliot
for line in file:
	#If the line contains elliot the a value
	#greater than -1 will be returned
	collection = ['elliot']
	if line.find("elliot, admin") > -1:
		print"Found elliot, logging record"
		#Open log file, write data from password, close file
		log = open("log.txt","w")
		log.write(line)
		log.close()
		#Exit loop
		break
	else:
		print "Nothing Fuond"

#Close file		
file.close()
#!/usr/bin/python

#Open file
file = open("data.txt","r")

#loop throught file
for line in file:
	print line

#close file
file.close()
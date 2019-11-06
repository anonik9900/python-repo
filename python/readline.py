#!/usr/bin/python

#Open File

file = open("data.txt","r")

#Read Line
print file.readline()

#Read x number of characters from file
print file.readline(3)

#close file
file.close()

#!/usr/bin/python

name = raw_input("Please enter your name:  ")
age = raw_input("Enter your age: ")
bday = raw_input ("Enter your Birthday: ")



def FinalData():
	print "Ti chiami "+name+ " Hai " +age+ " anni e sei nato il " +bday 
print FinalData()




ulogin = ""
ipass = ""

def displayWelcome():
	print "Welcome to the Private Area" 
	print ""

def getUserLogin():
	
	return  raw_input("Please enter your login name: ")
	

def getUserPass():

	return  raw_input("Please enter your password: ")


def displayLoginCred(login,password):
	print "Login: " + login
	print "password: " + password

displayWelcome()
ulogin = getUserLogin()
ipass = getUserPass()

displayLoginCred(ulogin,ipass)

	

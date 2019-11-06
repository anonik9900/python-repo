#!/usr/bin/python

# if -esle -Elif


val = 21

if val == 13:
	print "The value is 13"
elif val == 20:
	print "The value isn't 13, but 20"
else:
	print "a fan to culu"


password = "s3cre3t"
ulogin = ""
ipass = ""

def displayWelcome():
	print "Welcome to the Private Area" 
	print ""

def getUserLogin():
	
	return  raw_input("root@127.0.0.1: ")
	

def getUserPass():

	return  raw_input("Password: ")


def displayLoginCred(login,paswrd):
	print "Login: " + login
	print "password: " + paswrd

 
def checkPassword(paswrd):
	global password
	if paswrd == password:
		return "true";
	else:
		return "false";


displayWelcome()
ulogin = getUserLogin()
ipass = getUserPass()

print checkPassword(ipass);

#displayLoginCred(ulogin,ipass)
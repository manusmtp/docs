#!/usr/bin/python


#def printer(mylist):
#        for i in range(0,len(mylist)):
#                print mylist[i]

#mylist = map(str, raw_input("Enter your list : ").split(  )) 
#printer(mylist)
#print "The sum of numbers is: "+str(sum(mylist))


def printer(mylist):
	for i in range(0,len(mylist)):
		print mylist[i]

mylist = []
noc = raw_input("Number of commands:")
noco = int(noc)
for i in range(0,noco):
	mylist.append(raw_input("Enter command %d:" % ( i + 1 ) ) )

printer(mylist)

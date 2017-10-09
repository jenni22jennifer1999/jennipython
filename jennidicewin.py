#!/usr/bin/python3
import random  #importing random
count=0
r=0   #input
while count<=100:  #creating while loop
	roll=input("Press r to roll the dice:")  #input command
	if roll=="r":   #condition
		r=random.randint(1,6)  #gives random number betweem 1&6
		count=count+r  #increases the no. of count by r
		if count==8:   #condition
			count=37
			print("Your random number is ",r)     #gives the random number
			print("You are on a count ",count)     #gives the count
		elif count==13:
			print("Your random number is ",r)      #gives the random number    
			print("You are on a count ",count)
			count=34
			print("You climb on a ladder to ",count)
		elif count==40:
			print("Your random number is ",r)     #gives the random number
			print("You are on a count ",count)
			count=68
			print("You climb on a ladder to ",count)
		elif count==52:
			print("Your random number is ",r)     #gives the random number
			print("You are on a count ",count)
			count=81
			print("You climb on a ladder to ",count)
		elif count==76:
			print("Your random number is ",r)     #gives the random number
			print("You are on a count ",count)
			count=97
			print("You climb on a ladder to ",count)
		elif count==11:
			r=r+1
			print("Your random number is ",r)     #gives the random number
			count=count+r
			print("You are on count ",count)
		elif count==25:
			r=r+1
			print("Your random number is ",r)     #gives the random number
			count=count+r
			print("You are on count ",count)
		elif count==38:
			r=r+1
			print("Your random number is ",r)     #gives the random number
			count=count+r
			print("You are on count ",count)
		elif count==65:
			r=r+1
			print("Your random number is ",r)     #gives the random number
			count=count+r
			print("You are on count ",count)
		elif count==89:
			r=r+1
			print("Your random number is ",r)     #gives the random number
			count=count+r
			print("You are on count ",count)
		elif count==93:
			r=r+1
			print("Your random number is ",r)     #gives the random number
			count=count+r
			print("You are on count ",count)
		elif count==count:
			print("Your random number is ",r)     #gives the random number
			print("You are on count ",count)
	

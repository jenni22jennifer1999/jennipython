#!/usr/bin/python3
#snake and ladder.
import random    #importing random
count=0
r=0
while count<=100:  #while loop
	roll=input("Press r to roll the dice:")  #input command
	if roll=="r":
		r=random.randint(1,6)   #gives a random number from 1 to 6.
		count=count+r   #increases the count
		print("Your random number is ",r)     #prints the random no.
		if count==8:   #if condition
			print("You are on count ",count)
			count=37
			print("Yoru climb on a ladder to ",count)
		elif count==13:   #if else condition
			print("You are on count ",count)
			count=34
			print("You climb on a ladder to ",count)
		elif count==40:
			print("You are on count ",count)
			count=68
			print("You climb on a ladder to ",count)
		elif count==52:
			print("You are on count ",count)
			count=81
			print("You climb on a ladder to ",count)
		elif count==76:
			print("You are on count ",count)
			count=97
			print("You climb on a ladder to ",count)
		elif count==11:
			print("You are on count ",count)
			count=2
			print("You bit and climb down to ",count)
		elif count==25:
			print("You are on count ",count)
			count=4
			print("You bit and climb down to ",count)
		elif count==38:
			print("You are on count ",count)
			count=9
			print("You bit and climb down to ",count)
		elif count==65:
			print("You are on count ",count)
			count=46
			print("You bit and climb down to ",count)
		elif count==89:
			print("You are on count ",count)
			count=70
			print("You bit and climb down to ",count)
		elif count==93:
			print("You are on count ",count)
			count=64
			print("You bit and climb down to ",count)
		elif count==100:
			print("You are on count ",count)
			print("You are the winner.")
		else:
			print("You are on count ",count)
	

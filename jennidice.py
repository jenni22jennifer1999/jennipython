#!/usr/bin/python3
import random
count=0
r=0
while count<=100:
	roll=input("Press r to roll the dice:")
	if roll=="r":
		r=random.randint(1,6)
		count=count+r
		print("Your random number is ",r)
		if count==8:
			num=37
			c=num
			print("You are on count ",c)
		elif count==13:
			num=34
			c=num
			print("You are on count ",c)
		elif count==40:
			num=68
			c=num
			print("You are on count ",c)
		elif count==52:
			num=81
			c=num
			print("You are on count ",c)
		elif count==76:
			num=97
			c=num
			print("You are on count ",c)
		elif:
		    print("You are on count ",count)






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
			count=37
			print("You are on count ",count)
		elif count==13:
			count=34
			print("You are on count ",count)
		elif count==40:
			count=68
			print("You are on count ",count)
		elif count==52:
			count=81
			print("You are on count ",count)
		elif count==76:
			count=97
			print("You are on count ",count)
		elif count==count:
			print("You are on count ",count)
	





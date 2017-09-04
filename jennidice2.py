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
		elif count==11:
			count=2
			print("You are on count ",count)
		elif count==25:
			count=4
			print("You are on count ",count)
		elif count==38:
			count=9
			print("You are on count ",count)
		elif count==65:
			count=46
			print("You are on count ",count)
		elif count==89:
			count=70
			print("You are on count ",count)
		elif count==93:
			count=64
			print("You are on count ",count)
		elif count==count:
			print("You are on count ",count)
	
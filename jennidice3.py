#!/usr/bin/python3
import random
count=0
r=0
while count<=100:
	roll=input("Press r to roll the dice:")
	if roll=="r":
		r=random.randint(1,6)
		count=count+r
		if count==8:
			count=37
			print("Your random number is ",r)
			print("You are on count ",count)
		elif count==13:
			count=34
			print("Your random number is ",r)
			print("You are on count ",count)
		elif count==40:
			count=68
			print("Your random number is ",r)
			print("You are on count ",count)
		elif count==52:
			count=81
			print("Your random number is ",r)
			print("You are on count ",count)
		elif count==76:
			count=97
			print("Your random number is ",r)
			print("You are on count ",count)
		elif count==11:
			r=r+1
			print("Your random number is ",r)
			count=count+r
			print("You are on count ",count)
		elif count==25:
			r=r+1
			print("Your random number is ",r)
			count=count+r
			print("You are on count ",count)
		elif count==38:
			r=r+1
			print("Your random number is ",r)
			count=count+r
			print("You are on count ",count)
		elif count==65:
			r=r+1
			print("Your random number is ",r)
			count=count+r
			print("You are on count ",count)
		elif count==89:
			r=r+1
			print("Your random number is ",r)
			count=count+r
			print("You are on count ",count)
		elif count==93:
			r=r+1
			print("Your random number is ",r)
			count=count+r
			print("You are on count ",count)
		elif count==count:
			print("Your random number is ",r)
			print("You are on count ",count)
	
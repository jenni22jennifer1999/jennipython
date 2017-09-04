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
			print("You are on count ",count)
			count=37
			print("You climb on a ladder to ",count)
		elif count==13:
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
		elif count==count:
			print("You are on count ",count)
	
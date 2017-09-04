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
		print("You are on count ",count)

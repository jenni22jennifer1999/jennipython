#!/usr/bin/python3
import os  #importing os.
import time   #importing time.
a=0
b=1
while a<=10:  #creating while loop.
    os.system("fswebcam -F 5 --fps 20 -r \"1200x800\".jpg")  # capturing command.
    a=a+1
    b=b+1
    time.sleep(30)  # timings.

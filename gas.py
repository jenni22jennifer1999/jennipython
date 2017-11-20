#!/usr/bin/env python
import sys
import RPi.GPIO as GPIO
import time
# Pin Setup

def setup():
        GPIO.setmode(GPIO.BOARD) # GPIO Numbering of Pins
	GPIO.setup(19, GPIO.OUT) # Set pin number 19 as output
	GPIO.output(19, GPIO.LOW) # Set 19 to LOW to turn off the gas

def loop():
        while True:
            print ('GAS detected')
            GPIO.output(19,GPIO.HIGH)
            time.sleep(5,0)
            print ('COOL Environment')
            GPIO.output(19,GPIO.LOW)
            time.sleep(5,0)
def endprogram():

        GPIO.output(19, GPIO.LOW)   
        GPIO.cleanup()

if __name__ == '__main__':   Program starts here
        setup()
        try:
              
		loop()
        except KeyboardInterrupt:  # when 'ctrl-c is pressed
		endprogram()
 

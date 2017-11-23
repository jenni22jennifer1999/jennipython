import wiringpi
import RPi.GPIO as GPIO
import time

GAS_PIN = 19
GPIO.setmode(GPIO.BCM)
GPIO.setup(GAS_PIN,GPIO.IN)


while 1:
#    print ("Checking ...")
    val = GPIO.input(GAS_PIN)

    time.sleep(1)

#    print (val)

    if val==0:
        print("GAS detected")
        print("\n")
    else:
        print("Cool environment")
        print("\n")

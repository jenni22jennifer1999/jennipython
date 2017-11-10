from gpiozero import MotionSensor #importing motion sensor from gpiozero
import os #importing os
pir = MotionSensor(4)
while True: #while condition
    if pir.motion_detected:  #if statement
       r= print ("motion detected!") #printing statement
       if pir=="r"
        os.system("fswebcam -F 3 --fps 20 -r 1200x800 pir.jpg")  #image size and pixel
        

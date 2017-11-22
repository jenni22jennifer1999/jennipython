import wiringpi
wiringpi.pinMode(19,INPUT) 
#wiringPiSetupGpio()
pinMode(GAS_PIN,INPUT)

while(1):
    if(digitalRead(GAS_PIN)==LOW):
        print("GAS detected")
        print("\n")
    else:
        print("Cool environment")
        print("\n")
    delay(2000)
  

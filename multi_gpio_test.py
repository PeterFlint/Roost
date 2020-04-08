import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
import socket
 

class Lights():

    GPIO.setup(8,GPIO.OUT)
    
    def __init__(self, lights):
        self.lights = False
        self.lights = lights
        if self.lights == "True":
            print("LED on")
            GPIO.output(8,GPIO.LOW)
            return

        else:
            print("LED off")
            GPIO.output(8,GPIO.HIGH)
            return

class Motion():
    
    GPIO.setup(7,GPIO.IN)

    def __ini__(self, motion):
        self.motion = False
        self.motion = motion
        if self.motion == "True":
            try:
                GPIO.add_event_detect(7, GPIO.RISING)
                while 1:
                    time.sleep(1)
                    return
            except KeyboardInterrupt:
                print ("Quit")
                GPIO.cleanup()
        elif self.motion == "False":
            GPIO.cleanup()
            return
        else:
            print("An Error was recorded")


soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.connect(("192.168.1.3", 6666))
while True:
    message = soc.recv(1024)
    print(message.decode("utf-8"))

useLights = input("Boolian True or False")
useMotion = input("Boolian True or False") 
Lights(useLights)
Motion(useMotion)
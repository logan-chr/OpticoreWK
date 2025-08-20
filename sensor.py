import RPi.GPIO as GPIO
import time
class sensor():
    def __init__(self):
        self.status = False
        GPIO.setmode(GPIO.BCM)
        PIR_PIN = 4  
        GPIO.setup(PIR_PIN, GPIO.IN)

    def scan():
        
    
        if GPIO.input(4):
            
            return True
        else:
            return False


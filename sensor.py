import RPi.GPIO as GPIO
import time

def sense():
    GPIO.setmode(GPIO.BCM)
    PIR_PIN = 4  
    GPIO.setup(PIR_PIN, GPIO.IN)
    
    if GPIO.input(PIR_PIN):
            
        return True
    else:
        return False

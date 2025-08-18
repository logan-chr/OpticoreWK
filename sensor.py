import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)
PIR_PIN = 4  # Replace with the GPIO pin connected to the sensor
GPIO.setup(PIR_PIN, GPIO.IN)
n = 0
while True:
    if GPIO.input(PIR_PIN):
        n+= 1
        print(n)
    time.sleep(1)


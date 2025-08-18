import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)
PIR_PIN = 2  # Replace with the GPIO pin connected to the sensor
GPIO.setup(PIR_PIN, GPIO.IN)

print("Waiting for motion...")
try:
    while True:
        if GPIO.input(PIR_PIN):
            print("Motion detected!")
        time.sleep(1)
        
except KeyboardInterrupt:
    print("Exiting...")
finally:
    GPIO.cleanup()


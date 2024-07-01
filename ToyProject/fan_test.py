import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)

import RPi.GPIO as GPIO
import time

relayPin = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(relayPin, GPIO.OUT)

try:
	while True:
		print("FAN ON!")
		GPIO.output(relayPin, 1)
		time.sleep(5)
		print("FAN OFF!")
		GPIO.output(relayPin, 0)
		time.sleep(5)

except KeyboardInterrupt:
	GPIO.cleanup()

# title : ioh011_relay.py
# date : 2024-06-24
# desc : 릴레이 모듈 01

import RPi.GPIO as GPIO
import time

relayPin = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(relayPin, GPIO.OUT)

try:
	while True:
		GPIO.output(relayPin, 1)
		time.sleep(1)
		GPIO.output(relayPin, 0)
		time.sleep(1)

except KeyboardInterrupt:
	GPIO.cleanup()

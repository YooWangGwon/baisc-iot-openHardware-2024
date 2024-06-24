# title : module_test01.py
# date : 2024-06-24
# desc : 적외선 장애물 회피 센서

import RPi.GPIO as GPIO
import time

pin = 5

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.IN)

try:
	while True:
		if GPIO.input(pin) == False:
			print('Detected')
		time.sleep(0.005)

except KeyboardInterrupt:
	GPIO.cleanup()

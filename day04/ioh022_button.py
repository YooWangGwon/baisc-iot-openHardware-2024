import RPi.GPIO as GPIO
import time

Btn = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(Btn, GPIO.IN)

try:
	while True:
		if GPIO.input(Btn) == True:
			print("Clicked")
		time.sleep(1)

except KeyboardInterrupt:
	pass

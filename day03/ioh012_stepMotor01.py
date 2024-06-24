# title : ioh012_stepMotor01.py
# date : 2024-06-24
# desc : 스텝모터 01

import RPi.GPIO as GPIO
import time

steps = [21, 22, 23, 24]

GPIO.setmode(GPIO.BCM)

for stepPin in steps:
	GPIO.setup(stepPin, GPIO.OUT)
	GPIO.output(stepPin, 0)

try:
	while 1:
		GPIO.output(steps[0],0)
		GPIO.output(steps[1],0)
		GPIO.output(steps[2],0)
		GPIO.output(steps[3],1)
		time.sleep(0.005)

		GPIO.output(steps[0],0)
		GPIO.output(steps[1],0)
		GPIO.output(steps[2],1)
		GPIO.output(steps[3],1)
		time.sleep(0.005)

		GPIO.output(steps[0],0)
		GPIO.output(steps[1],0)
		GPIO.output(steps[2],1)
		GPIO.output(steps[3],0)
		time.sleep(0.005)

		GPIO.output(steps[0],0)
		GPIO.output(steps[1],1)
		GPIO.output(steps[2],1)
		GPIO.output(steps[3],0)
		time.sleep(0.005)

		GPIO.output(steps[0],0)
		GPIO.output(steps[1],1)
		GPIO.output(steps[2],0)
		GPIO.output(steps[3],0)
		time.sleep(0.005)

		GPIO.output(steps[0],1)
		GPIO.output(steps[1],1)
		GPIO.output(steps[2],0)
		GPIO.output(steps[3],0)
		time.sleep(0.005)

		GPIO.output(steps[0],1)
		GPIO.output(steps[1],0)
		GPIO.output(steps[2],0)
		GPIO.output(steps[3],0)
		time.sleep(0.005)

		GPIO.output(steps[0],1)
		GPIO.output(steps[1],0)
		GPIO.output(steps[2],0)
		GPIO.output(steps[3],1)
		time.sleep(0.005)

except KeyboardInterrupt:
	GPIO.cleanup()

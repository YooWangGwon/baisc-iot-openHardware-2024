# title : ioh012_stepMotor02.py
# date : 2024-06-24
# desc : 스텝모터 02

import RPi.GPIO as GPIO
import time

steps = [21, 22, 23, 24]

GPIO.setmode(GPIO.BCM)

for stepPin in steps:
	GPIO.setup(stepPin, GPIO.OUT)
	GPIO.output(stepPin, 0)

# 전자석 위치 리스트
Seq = [[0,0,0,1],[0,0,1,1],[0,0,1,0],[0,1,1,0],[0,1,0,0],[1,1,0,0],[1,0,0,0],[1,0,0,1]]


StepCounter = 0
StepCount = 8

try:
	while 1:
		for i in range(0,4):
			xPin = steps[i]

			# 코일에 전류를 흘리는 부분
			if Seq[StepCounter][i] != 0:
				GPIO.output(xPin, 1)
			else:
				GPIO.output(xPin, 0)

		# 
		StepCounter += 1

		if(StepCounter == StepCount):
			StepCounter = 0
		if(StepCounter < 0):
			StepCounter = StepCount

		time.sleep(0.001)

except KeyboardInterrupt:
	print('step motor OFF!!')
	GPIO.cleanup()

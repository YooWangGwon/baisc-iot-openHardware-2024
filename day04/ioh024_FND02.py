# title : ioh023_FND01.py
# date : 2024-06-25
# desc : FND 제어 연습

import RPi.GPIO as GPIO
import time

a = 20
b = 21
c = 22
d = 23
e = 24
f = 25
g = 26
dp = 19

led = [a,b,c,d,e,f,g,dp]
set = [[0,1,1,0,0,0,0,0],[1,1,0,1,1,0,1,0],[1,1,1,1,0,0,1,0],[0,1,1,0,0,1,1,0],
[1,0,1,1,0,1,1,0],[1,0,1,1,1,1,1,0],[1,1,1,0,0,1,0,0],
[1,1,1,1,1,1,1,0],[1,1,1,1,0,1,1,0],[1,1,1,1,1,1,0,0]]

GPIO.setmode(GPIO.BCM)

for i in range(0,8):
	GPIO.setup(led[i], GPIO.OUT)

#GPIO.setup(g, GPIO.OUT)
#GPIO.setup(dp, GPIO.OUT)

try:
	while True:
		for i in range(0,10):
			GPIO.output(a, set[i][0])
			GPIO.output(b, set[i][1])
			GPIO.output(c, set[i][2])
			GPIO.output(d, set[i][3])
			GPIO.output(e, set[i][4])
			GPIO.output(f, set[i][5])
			GPIO.output(g, set[i][6])
			GPIO.output(dp, set[i][7])

			time.sleep(1)

except KeyboardInterrupt:
	print('FND OFF!')
	GPIO.cleanup()

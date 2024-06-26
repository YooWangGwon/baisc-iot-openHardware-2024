# title : ioh026_FND04.py
# date : 2024-06-26
# desc : FND 제어 연습 4

# 0.5초마다 FND 4Digit에 표시되는 값이 1씩 증가

from multiprocessing import Process, Queue
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

com1 = 18
com2 = 17
com3 = 13
com4 = 12

a = 20
b = 21
c = 22
d = 23
e = 24
f = 25
g = 26
dp = 19

led = [a,b,c,d,e,f,g,dp]
com = [com1, com2, com3, com4]

# 숫자 표시에 사용할 값 리스트의 리스트
set = [[1,1,1,1,1,1,0,0],[0,1,1,0,0,0,0,0],[1,1,0,1,1,0,1,0],[1,1,1,1,0,0,1,0],[0,1,1,0,0,1,1,0],
[1,0,1,1,0,1,1,0],[1,0,1,1,1,1,1,0],[1,1,1,0,0,1,0,0],
[1,1,1,1,1,1,1,0],[1,1,1,1,0,1,1,0]]

def arrange_num(num):
	str_num = str(num).zfill(4)
	for i in range(0, 4):
		show_num(i, int(str_num[i]))

def show_num(pos, num):
	GPIO.output(com[pos], GPIO.LOW)
	for i in range(0,8):
		GPIO.output(led[i], set[num][i])
	time.sleep(0.005)
	GPIO.output(com[pos], GPIO.HIGH)

def setup():
	for n in range(0,8):
		GPIO.setup(led[n], GPIO.OUT)
		GPIO.output(led[n], 0)

	for n in range(0,4):
		GPIO.setup(com[n], GPIO.OUT)
		GPIO.output(com[n], 1)

if __name__ == "__main__":
	setup()
	try:
		count = 0
		while True:
			for _ in range(200):
				time.sleep(0.5)
			count = (count + 1) % 10000

	finally:
		GPIO.cleanup()

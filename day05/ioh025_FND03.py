# title : ioh025_FND03.py
# date : 2024-06-26
# desc : FND 제어 연습

# 버튼을 클릭하면 FND 출력 숫자 변경

import RPi.GPIO as GPIO
import time

btn = 4

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

def show_num(pos, num):
	for i in range(0,4):
		if i + 1 == pos:
			GPIO.output(com[i], 0)
		else:
			GPIO.output(com[i], 1)
	for i in range(0,8):
		GPIO.output(led[i], set[num][i])

GPIO.setmode(GPIO.BCM)

for n in range(0,8):
	GPIO.setup(led[n], GPIO.OUT)

for n in range(0,4):
	GPIO.setup(com[n], GPIO.OUT)

GPIO.setup(btn, GPIO.IN)

count = 0
thcount = 0
hcount = 0
tcount = 0
ocount = 0

try:
	while True:
		if GPIO.input(btn) == True:
			count += 1
			if count > 9999:
				count = 0
			thcount = count // 1000
			hcount = count % 1000 // 100
			tcount = count % 100 // 10
			ocount = count % 10
			time.sleep(0.5)

		elif GPIO.input(btn) == False:
			show_num(1,thcount)
			time.sleep(0.001)
			show_num(2,hcount)
			time.sleep(0.001)
			show_num(3,tcount)
			time.sleep(0.001)
			show_num(4,ocount)
			time.sleep(0.001)


except KeyboardInterrupt:
	print('FND OFF!')
	GPIO.cleanup()

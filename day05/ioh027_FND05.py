# title : ioh026_FND05.py
# date : 2024-06-26
# desc : FND 제어 연습 5

# 1초마다 FND 4Digit에 표시되는 값이 1씩 증가

import RPi.GPIO as GPIO
import time

# FND Digit 핀 설정
com1 = 18
com2 = 17
com3 = 13
com4 = 12

# FND Segment 핀 설정
a = 20
b = 21
c = 22
d = 23
e = 24
f = 25
g = 26
dp = 19

segment_pins = [a,b,c,d,e,f,g,dp]
digit_pins = [com1, com2, com3, com4]

# 숫자 표시에 사용할 값 세그먼트 패턴
segment_patterns = [[1,1,1,1,1,1,0,0],[0,1,1,0,0,0,0,0],[1,1,0,1,1,0,1,0],
	[1,1,1,1,0,0,1,0],[0,1,1,0,0,1,1,0],
	[1,0,1,1,0,1,1,0],[1,0,1,1,1,1,1,0],
	[1,1,1,0,0,1,0,0],[1,1,1,1,1,1,1,0],
	[1,1,1,1,0,1,1,0]]

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    for pin in segment_pins:	# 세그먼트 핀을 출력 모드로 설정
        GPIO.setup(pin, GPIO.OUT)
    for pin in digit_pins:	# 출력되는 핀을 출력모드로 설정 및 초기상태를 HIGH로 지정
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.HIGH)

def display_number(number):
	digits = [int(d) for d in str(number).zfill(4)]	# 각 자리의 숫자를 문자 형태로 분할
	# 각 자리마다 순차적인 출력 시작
	for i in range(4):
		GPIO.output(digit_pins[i], GPIO.LOW)	# 출력할 자릿수를 LOW로 변경하여 전류가 흐를 수 있게 설정
		pattern = segment_patterns[digits[i]]	# 해당 자릿수에 출력할 숫자를 표현하는 0과 1의 패턴  리스트를 가져옴
		for pin, state in zip(segment_pins, pattern):	# segment_pin의 순서와 패턴 리스트 순서에 맞게 작업 시작
			GPIO.output(pin, state)
		time.sleep(0.005)	# 숫자가 표시되고 0.005초 대기
		GPIO.output(digit_pins[i], GPIO.HIGH)	# 출력한 자릿수를 다시 HIGH로 변경

def main():
	setup()	# GPIO 핀 초기화
	try:
		for number in range(1, 10000): # 1에서 9999까지 숫자 범위 안에서
			start_time = time.time()	# 현재 시간을 초 단위로 저장
			while time.time() - start_time < 1:	# 1초 동안 숫자를 계속 표시
				display_number(number)
	except KeyboardInterrupt:
		print("")
	finally:
		GPIO.cleanup()

if __name__ == '__main__':
	main()

# title : ioh030_FND08.py
# date : 2024-06-27
# desc : FND 제어 연습 8

import RPi.GPIO as GPIO
import time

# Segment(led pin)
segment_pins = [20, 21, 22, 23, 24, 25, 26, 19] # a ~ dp
# Digit
digit_pins = [18, 17, 13, 12]	# COM1 ~ COM2
# 0~9 까지 1byte hex값
segment_patterns = [0x3f, 0x06, 0x5b, 0x4f, 0x66, 0x6d, 0x7d, 0x27, 0x7f, 0x6f]

def setup():
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
	for pin in segment_pins:	# 세그먼트 핀을 출력 모드로 설정
		GPIO.setup(pin, GPIO.OUT)
		GPIO.output(pin, 0)
	for pin in digit_pins:# 출력되는 핀을 출력모드로 설정 및 초기상태를 HIGH로 지정
		GPIO.setup(pin, GPIO.OUT)
		GPIO.output(pin, 1)

def fndOut(data, sel):	# 하나의 숫자 형태를 만드는 함수
	for	i in range(0, 7):
		GPIO.output(segment_pins[i], segment_patterns[data] & (0x01 << i))
		for j in range(3, -1, -1):	# 자릿수의 FND만 켜질 수 있도록
			if j == sel:
				GPIO.output(digit_pins[j], 0)
			else:
				GPIO.output(digit_pins[j], 1)

count = 0

if __name__ == '__main__':
	setup()
	try:
		while True:
			count += 1
			d1000 = count // 1000
			d100 = count % 1000 // 100
			d10 = count % 100 // 10
			d1 = count % 10
			d = [d1000, d100, d10, d1]

			#for _ in range(250):	# 0.004초를 250번 반복 -> 1초
			for i in range(3, -1, -1):
				fndOut(int(d[i]), i)
				time.sleep(0.001)

			if count == 9999:
				count = -1

	except KeyboardInterrupt:
		print('FND OFF')
		GPIO.cleanup()

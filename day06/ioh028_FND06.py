# title : ioh026_FND06.py
# date : 2024-06-27
# desc : FND 제어 연습 6

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

def fndOut(data):	# 하나의 숫자 형태를 만드는 함수
	for	i in range(0, 7):
		GPIO.output(segment_pins[i], segment_patterns[data] & (0x01 << i))

if __name__ == '__main__':
	setup()
	try:
		while True:
			for i in range(0, 1):
				GPIO.output(digit_pins[i], 0)

				for j in range(0,10):
					fndOut(j)
					time.sleep(0.5)

	except KeyboardInterrupt:
		print('FND OFF')
		GPIO.cleanup()

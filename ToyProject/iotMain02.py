import sys
import RPi.GPIO as GPIO
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTimer
from PyQt5 import uic
import adafruit_dht
import board
import time
import datetime as dt


form_class = uic.loadUiType("iotProgram.ui")[0]
leds = [4,5,6]	# red, green, blue
dht_pin = 16
piezo_pin = 27
fan_pin = 18

# FND Digit 핀 설정
# com1 = 18
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
digit_pins = [com2, com3, com4]

# 숫자 표시에 사용할 값 세그먼트 패턴
segment_patterns = [[1,1,1,1,1,1,0,0],[0,1,1,0,0,0,0,0],[1,1,0,1,1,0,1,0],
	[1,1,1,1,0,0,1,0],[0,1,1,0,0,1,1,0],
	[1,0,1,1,0,1,1,0],[1,0,1,1,1,1,1,0],
	[1,1,1,0,0,1,0,0],[1,1,1,1,1,1,1,0],
	[1,1,1,1,0,1,1,0]]

def display_number(number):
	digits = [int(d) for d in str(number).zfill(3)]	# 각 자리의 숫자를 문자 형태로 분할
	# 각 자리마다 순차적인 출력 시작
	for i in range(3):
		GPIO.output(digit_pins[i], GPIO.LOW)	# 출력할 자릿수를 LOW로 변경하여 전류가 흐를 수 있게 설정
		pattern = segment_patterns[digits[i]]	# 해당 자릿수에 출력할 숫자를 표현하는 0과 1의 패턴  리스트를 가져옴
		for pin, state in zip(segment_pins, pattern):	# segment_pin의 순서와 패턴 리스트 순서에 맞게 작업 시작
			GPIO.output(pin, state)
		time.sleep(0.005)	# 숫자가 표시되고 0.005초 대기
		GPIO.output(digit_pins[i], GPIO.HIGH)	# 출력한 자릿수를 다시 HIGH로 변경

# WindowClass 선언
class WindowClass(QMainWindow, form_class):
	def __init__ (self):	# 생성자, 첫번째 인자는 자기자신을 의미하는 self
		super().__init__()	# 부모 클래스 생성자(QWidget이 부모클래스이므로 QWidget의 생성자임)
		self.setupUi(self)
		self.humid = 0
		self.temp = 0

		# GPIO & sensor setting

		GPIO.setmode(GPIO.BCM)
		for pin in leds:
			GPIO.setup(pin, GPIO.OUT)
		GPIO.setup(dht_pin, GPIO.IN)
		GPIO.setup(piezo_pin, GPIO.OUT)
		GPIO.setup(fan_pin, GPIO.OUT)

		for pin in segment_pins:	# 세그먼트 핀을 출력 모드로 설정
			GPIO.setup(pin, GPIO.OUT)
		for pin in digit_pins:	# 출력되는 핀을 출력모드로 설정 및 초기상태를 HIGH로 지정
			GPIO.setup(pin, GPIO.OUT)
			GPIO.output(pin, GPIO.HIGH)

		# DHT 센서 연결
		self.sensor = adafruit_dht.DHT11(board.D16)
		self.Buzz = GPIO.PWM(piezo_pin, 440)

		# timer for DHT sensor
		self.timer = QTimer(self)
		self.timer.timeout.connect(self.update_data)
		self.timer.timeout.connect(self.module_con)
		self.timer.start()

	# DHT 센서에서 온습도 정보 가져오기
	def update_data(self):
		try:
			humidity = self.sensor.humidity
			temperature = self.sensor.temperature
			self.temp = temperature
			self.humid = humidity
			datetime = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
			if humidity is not None and temperature is not None:
				self.Lbl_time.setText(datetime)
				self.LCD_temp.display(temperature)
				self.LCD_humid.display(humidity)
				print(f'{datetime} -> Temperature: {temperature:.1f}C Humidity: {humidity:.1f}%')
			else:
				self.textEdit1.setText('Temperature: Error')
				self.textEdit1.setText('Humidity: Error')
				print(f'{datetime} -> Temperature: {temperature}C Humidity: {humidity}%')
				print("Error Occured!!")

		except RuntimeError as ex:
			print(ex.args[0])

	# 가져온 온습도 정보를 바탕으로 모듈 작동
	def module_con(self):
		value = self.humidLevel.value()
		if self.humid > value and self.Chb_warning.isChecked():
			try:
				GPIO.output(fan_pin, 1)
				print("FAN ON!!")
				self.Buzz.start(25)
				for _ in range(3):
					self.Buzz.ChangeFrequency(200)

					self.btn1Function()
					start_time1 = time.time()
					while time.time() - start_time1 < 0.5:
						display_number(int(self.humid))

					self.Buzz.ChangeFrequency(400)
					self.btn2Function()
					start_time2 = time.time()
					while time.time() - start_time2 < 0.5:
						display_number(int(self.humid))
				self.Buzz.stop()
			except RuntimeError as ex:
				print(ex.args[0])
		else:
			GPIO.output(fan_pin, 0)
			print("FAN OFF!!")
			self.btn3Function()
			for _ in range(300):
				display_number(int(self.humid))

	def btn1Function(self):	# Red
		print("Red LED ON!!")
		GPIO.output(leds[0], False)
		GPIO.output(leds[1], True)
		GPIO.output(leds[2], True)

	def btn2Function(self):	# Blue
		print("Blue LED ON!!")
		GPIO.output(leds[0], True)
		GPIO.output(leds[1], True)
		GPIO.output(leds[2], False)

	def btn3Function(self): # Green
		print("Green LED ON!!")
		GPIO.output(leds[0], True)
		GPIO.output(leds[1], False)
		GPIO.output(leds[2], True)

	def btn4Function(self):
		print("LED OFF!!")
		GPIO.output(leds[0], True)
		GPIO.output(leds[1], True)
		GPIO.output(leds[2], True)

	def closeEvent(self, event) -> None:
		re = QMessageBox.question(self, 'Exit', 'Do you want to exit?', QMessageBox.Yes | QMessageBox. No)
		if re == QMessageBox.Yes:
			event.accept()
			self.sensor.exit()
			GPIO.cleanup()

		else:
			event.ignore()

if __name__ == "__main__":
	#setup()
	app = QApplication(sys.argv)	# 프로그램을 실행시키는 클래스
	myWindow = WindowClass()		# WindowClass() 인스턴스 생성
	myWindow.show()					# 화면 보여주기
	app.exec_()						# 프로그램 실행
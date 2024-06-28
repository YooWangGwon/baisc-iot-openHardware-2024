# title : ioh032_qt02.py
# date : 2024-06-27
# desc : PyQt 연습 2

import sys
import RPi.GPIO as GPIO
from PyQt5.QtWidgets import *
from PyQt5 import uic
import time
import adafruit_dht
import board


led_pin = [4,5,6]	# red, green, blue
DHT_pin = 16
log_num = 0


form_class = uic.loadUiType("./iotProgram.ui")[0]

GPIO.setmode(GPIO.BCM)
for pin in led_pin:
	GPIO.setup(pin, GPIO.OUT)
GPIO.setup(DHT_pin, GPIO.IN)
dhtDevice = adafruit_dht.DHT11(board.D16)

# WindowClass 선언
class WindowClass(QMainWindow, form_class):
	def __init__ (self):	# 생성자, 첫번째 인자는 자기자신을 의미하는 self
		super().__init__()	# 부모 클래스 생성자(QWidget이 부모클래스이므로 QWidget의 생성자임)
		self.setupUi(self)

		# 이벤트  함수 등록
		self.Btn1.clicked.connect(self.btn1Function)
		self.Btn2.clicked.connect(self.btn2Function)
		self.Btn3.clicked.connect(self.btn3Function)
		self.Btn4.clicked.connect(self.btn4Function)
		self.DHT_ON.clicked.connect(self.DHT_onFunc)
	# LED 관련 함수

	def btn1Function(self):
		print("Red LED Button Clicked!!")
		GPIO.output(led_pin[0], False)
		GPIO.output(led_pin[1], True)
		GPIO.output(led_pin[2], True)

	def btn2Function(self):
		print("Blue LED Button Clicked!!")
		GPIO.output(led_pin[0], True)
		GPIO.output(led_pin[1], True)
		GPIO.output(led_pin[2], False)

	def btn3Function(self):
		print("Green LED Button Clicked!!")
		GPIO.output(led_pin[0], True)
		GPIO.output(led_pin[1], False)
		GPIO.output(led_pin[2], True)

	def btn4Function(self):
		print("Red LED Button Clicked!!")

		GPIO.output(led_pin[0], True)
		GPIO.output(led_pin[1], True)
		GPIO.output(led_pin[2], True)

	# DHT 관련 함수

	def DHT_onFunc(self):
		try:
			log_num += 1
			temp = dhtDevice.temperature
			humid = dhtDevice.humidity
			#self.textEdit1.setText(f'{log_num} - Temp : {temp}C / Humid : {humid}%\n')
			print(f'{log_num} - Temp : {temp}C / Humid : {humid}%\n')
			log_num += 1
		except RuntimeError as ex:
			print(ex.args[0])

	def DHT_offFunc(self):
		print('DHT OFF!!!')
		dhtDevice.exit()


	def slot1(self):
		GPIO.cleanup()
		print("EXIT")

if __name__ == "__main__":
	app = QApplication(sys.argv)	# 프로그램을 실행시키는 클래스
	myWindow = WindowClass()		# WindowClass() 인스턴스 생성
	myWindow.show()					# 화면 보여주기
	app.exec_()						# 프로그램 실행

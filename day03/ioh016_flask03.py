# title : ioh016_flask03.py
# date : 2024-06-24
# desc : flask 연습

# URL 접속을 /led/on. /led/off 로 접속하면 led를 on. off 하는 웹페이지 만들기

import RPi.GPIO as GPIO
from flask import Flask

led = 13

GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)

app = Flask(__name__)

@app.route("/")
def index():
	return "Hello LED Controller"

@app.route("/led/on")
def ledon():
	GPIO.output(led, False)
	return "LED ON"

@app.route("/led/off")
def ledoff():
	GPIO.output(led, True)
	return	"LED OFF"

if __name__ == "__main__":
	try:
		app.run(host = "0.0.0.0")

	except KeyboardInterrupt:
		print("System OFF!!")
		GPIO.cleanup()

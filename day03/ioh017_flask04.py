# title : ioh016_flask04.py
# date : 2024-06-24
# desc : 변수를 활용한 flask 연습

import RPi.GPIO as GPIO
from flask import Flask

led = 13

GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)

app = Flask(__name__)

@app.route("/")
def index():
	return "Hello LED Controller"

@app.route("/led/<state>")
def led_control(state):
	if state == "on":
		GPIO.output(led, False)
		return "<h1>LED ON</h1>"

	elif state == "off":
		GPIO.output(led, True)
		return	"<h1>LED OFF</h2>"

	elif state == "clear":
		GPIO.cleanup()
		return "GPIO cleanup()"
	else:
		return "LED Controller"

if __name__ == "__main__":
	try:
		app.run(host = "0.0.0.0", debug=True)

	except KeyboardInterrupt:
		print("System OFF!!")
		GPIO.cleanup()

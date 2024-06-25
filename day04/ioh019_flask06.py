# title : ioh019_flask06.py
# date : 2024-06-24
# desc : HTML를 활용한 flask 연습

import RPi.GPIO as GPIO
from flask import Flask, request, render_template

led = 13

GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/data", methods = [ 'POST' ])
def led_control():
	state = request.form['led']
	if state == "on":
		GPIO.output(led, False)
		return index()

	elif state == "off":
		GPIO.output(led, True)
		return index()

if __name__ == "__main__":
	try:
		app.run(host = "0.0.0.0", debug=True)

	except KeyboardInterrupt:
		print("System OFF!!")
		GPIO.cleanup()

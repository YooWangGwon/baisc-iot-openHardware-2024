# 정적 라우팅

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
	return "Hello Flask!"

@app.route("/name")
def name():
	return "<h1>my name is Yoo WangGwon</h1>"

@app.route("/age")
def age():
	return "<h1> 26 years old</h1>"

if __name__ == "__main__":
	app.run(host = "0.0.0.0", port="10011", debug=True)

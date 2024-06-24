# title : ioh018_flask05.py
# date : 2024-06-24
# desc : GET 방식 데이터 전달

# 주소전달 방법 : 주소/?이름=James&주소=Busan

from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def get():
	value1 = request.args.get("이름","user")
	value2 = request.args.get("주소","부산")
	return value1+ ":" + value2

if __name__ == "__main__":
	app.run(host = "0.0.0.0", port="18080", debug = True)

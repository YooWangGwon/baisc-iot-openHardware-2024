# title : ioh014_flask01.py
# date : 2024-06-24
# desc : Flask 연습

from flask import Flask # name 이름을 통한 flask 객체 생성

app = Flask(__name__)

@app.route("/")	# 라우팅을 위한 뷰 함수
def hello():	# 등록 사이트에 접속을 성공한다면 hello 함수 실행
	return "Hello World!"

if __name__ == "__main__":	# 터미널에서 직접 실행시키면 실행 파일이 main으로 바뀜
	app.run(host="0.0.0.0", port="10111", debug=True)

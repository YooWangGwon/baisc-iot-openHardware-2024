# baisc-iot-openHardware-2024
부경대학교 2024 IoT 개발자 과정 Iot 오픈하드웨어 플랫폼 활용

## 1일차(24.06.20)
- 기본 개념
    - 옴의 법칙 : V(전압) = I(전류)*R(저항)
        - 전압(V) : 전기장 안에서 전하가 갖는 전위의 차이(전위차)
        - 전류(I) : 높은 전압에서 낮은 전압으로 흐른
        - 저항(R) : 도체에서 전류의 흐름을 방해하는 정도
        - Vcc 전압 : 전원 IC가 동작하기 위한 전원
        - GND : 전류를 모이게 함(모든 전류는 그라운드로 흐름, 그라운드가 0V이기 때문), 기준전압이라고도 함
        - Vcc -> ON, GND -> OFF 
        - 라즈베리파이에 모듈을 연결할 때 DATA 선들을 먼저 연결하고나서 VCC 연결 후, GND 연
    
    - 키르히호프의 법칙 
        - 키르히호프의 전류 법칙(KCL)
            - 지점의 법칙, 분기점 법칙
            - 전류가 통과하는 분기점(선의 연결지점)에서 전류의 합(들어온 전류의 양과 나간 전류의 양)은 같다. 즉 0 이다.
        - 키르히호프의 전압 법칙
            - 루프의 법칙
            - 닫힌 하나의 루프안 전압(전위차)의 합은 0이다.
            - 폐쇄된 회로의 인가된 전원의 합과 분배된 전위의 차의 합은 그 루프 안에서 등가한다.

- 라즈베리파이 Python 함수
    - GPIO 설정함수(Python)
        - GPIO.setmode(GPIO.BOARD) - wPi
        - GPIO.setmode(GPIO.BCM) - BCM
        - GPIO.setup(channel, GPIO.mode) - channel : 핀번호, mode : IN/OUT
    
    - GPIO 출력함수
        - GPIO.output(channel, state)
        - channel : 핀번호
        - state : HIGH/LOW or 1/0 or True/False
    - GPIO 입력함수
        - GPIO.input(channel)
        - channel : 핀번호
        - 반환값 : HIGH/LOW or 1/0 or True/False
    - 시간지연 함수
        - time.sleep(secs)

- 스위치
    - 플로팅
        - 떠 있는 상태
        - 전류가 흐르는지 흐르지 않는지 알 수 없는 상태
    - 풀업 저항
        - 저항을 Vcc에 붙여 플로팅을 해결하는 방법
        - 스위치가 열려있으면 입력핀으로 전류가 흐르고 5V 전압이 걸리게 됨
        - 스위치가 닫혀있으면 모든 전류가 GND로 흐르고 입력핀에는 0V 전압이 걸리게 됨

    - 풀다운 저항 
        - 저항을 그라운드(GND)에 붙여 플로팅을 해결하는 방법
        - 스위치가 열려있으면 어디에도 전류가 공급되지 않는 상태
        - 스위치가 닫혀있으면 입력핀으로 전류가 흐르고 5V 전압이 걸리게됨
        
    <img src="https://raw.githubusercontent.com/YooWangGwon/baisc-iot-openHardware-2024/main/images/ioh001.png">


- 인터룹트(interrupt)
    - 어떤 상황에서도 제일 우선적으로 실행되는 동작

## 2일차(24.06.21)
- 라즈베리 파이 파이썬
    - 가상환경
        - python -V : 파이썬 버전 확인
        - python -m venv env(가상환경명) : 가상환경 env 생성
        - python -m venv --system-site-packages env : 옵션이 포함된 가상환경 env 생성
        - source ./env/bin/activate : 가상환경 실행
        - pip install '라이브러리 명'
        - deactivate : 가상환경 실행 중지(빠져나오기)
    
    - Wiring
        - 라즈베리파이에서 GPIO에 접근하는 방법
        - https://github.com/Wiring/Wiring
        - Wiring 폴더 안에서 ./bulid 실행
        - gpio readall : 라즈베리파이의 gpio에 대한 핀 정보가 출력

## 3일차(24.06.24)
- 릴레이 모듈
    - 용도 : 신호를 만들어내어 자동으로 ON/OFF를 조정하는 스위치 역할의 모듈
    - 사용 모듈 : 1채널 5V 미니 릴레이 모듈
    - NO(열린 접점) : 평상시에 열려있음, 신호가 가면 닫힘
    - NC(닫힌 접점) : 평상시에 닫혀있음, 신호가 가면 열림
    - 예시(LED모듈 스위치)
        - 릴레이 모듈 S : GPIO 연결
        - 릴레이 모듈 + : 5V 연결
        - 릴레이 모듈 - : GND 연결
        - 릴레이 모듈 COM : 5V 연결
        - 릴레이 모듈 NO or NC : LED 모듈의 VCC와 연결
        - LED 모듈 RGB : GND 연결

    <img src="https://raw.githubusercontent.com/YooWangGwon/baisc-iot-openHardware-2024/main/images/ioh002.jpg">

- 스텝 모터와 모터 드라이버
    - 스텝 모터 : 한 바퀴의 회전을 많은 수의 스텝 들로 나눌 수 있는 앙페르의 오른손 법칙을 활용한 브러쉬리스 직류 전기 모터
    - 앙페르의 오른손 법칙 : 
    - 모터 드라이버 : 스텝 모터를 원활하게 제어하기 위한 장치
    - 모터를 라즈베리 파이에 직접 연결하지 말것(모터의 전원이 종료될 때 연기전력이 발생되기 때문)
    - 스텝 모터 작동 방식
        - 1상 여자 방식 : 차례로 1개으 상에 전기 신호를 줌
        - 2상 여자 방식 : 동시에 2개의 상에 전기 신호를 줌
        - 1-2상 여자 방식 : 1상과 2상 방식을 반복

    - 예시
        - 모터 드라이버 + : 5V 연결
        - 모터 드라이버 - : GND 연결
        - 모터 드라이버 IN1 ~ IN4 : 각각의 GPIO에 연결

    <img src="https://raw.githubusercontent.com/YooWangGwon/baisc-iot-openHardware-2024/main/images/ioh003.jpg">
    

- Flask
    - 웹 애플리케이션 개발을 위한 파이썬 프레임워크

    ```python
    from flask import Flask # name 이름을 통한 flask 객체 생성
    app = Flask(__name__)

    @app.route("/") # 라우팅을 위한 뷰 함수
    def hello():    # 등록 사이트에 접속을 성공한다면 hello 함수 실행
    return "Hello World!"

    if __name__ == "__main__":  # 터미널에서 직접 실행시키면 실행 파일이 main으로 바뀜
        app.run(host="0.0.0.0", port="10111", debug=True)
    ```

    - GET 방식 데이터 전달 방법

    ```python
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
    ```
## 4일차(24.06.24)
- 카메라 모듈
    <img src="https://raw.githubusercontent.com/YooWangGwon/baisc-iot-openHardware-2024/main/images/ioh004.jpg">
- FND 모듈

    <img src="https://raw.githubusercontent.com/YooWangGwon/baisc-iot-openHardware-2024/main/images/ioh005.png">

    - 화면에 표시되는 Digit(COM1~COM2)과 Segmentation(a ~ dp)으로 구성

    - 작동 방식
        - 4-digit 규격의 공통 음극(Common Cathod)방식
            - Segmentation : VCC(HIGH)
            - Digit : GND(LOW)

            <img src="https://raw.githubusercontent.com/YooWangGwon/baisc-iot-openHardware-2024/main/images/ioh006.png">
            

        - 4-digit 규격의 공통 양극(Common Anode)방식
            - Segmentation : GND(LOW)
            - Digit : VCC(HIGH)

            <img src="https://raw.githubusercontent.com/YooWangGwon/baisc-iot-openHardware-2024/main/images/ioh007.png">



## 5일차(24.06.24)
- FND 모듈
    - 버튼을 클릭하면 FND에 표시되는 숫자가 올라가는 기능 구현
    - 1초마다 FND에 표시되는 숫자가 올라가는 기능 구현

    <img src="https://raw.githubusercontent.com/YooWangGwon/baisc-iot-openHardware-2024/main/images/ioh008.jpg">

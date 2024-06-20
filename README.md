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
        
    <img src="https://raw.githubusercontent.com/YooWangGwon/basic-iot-openHardware-2024/main/images/ioh001.png">


- 인터룹트(interrupt)
    - 어떤 상황에서도 제일 우선적으로 실행되는 동작
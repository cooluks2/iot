# picamera 라이브러리 임포트
import picamera

# time 라이브러리 임포트
import time

# PiCamera 객체 인스턴스 생성
with picamera.PiCamera() as camera:

    # 해상도를 선택하도록 함
    res = int(input('Resolution(1:320x240, 2:640x480, 3:1024x768)?'))
    
    # 선택한 값에 따라 해상도 설정
    if res == 3:
        camera.resolution = (1024, 768)
    elif res == 2:
        camera.resolution = (640, 480)
    else:
        camera.resolution = (320, 240)

    # 파일명 입력 받기
    filename = input('File Name?')

    # 프리뷰 화면 표시
    camera.start_preview()

    # 1초 대기
    time.sleep(1)

    # 프리뷰 종료
    camera.stop_preview()
    
    # 촬영하고 저장
    camera.capture(filename + '.jpg')

# python-picamera 3 동영상 촬영

**기본**

picam_video_ex01.py

```python
import picamera

camera = picamera.PiCamera()
camera.resolution = (640, 480)

camera.start_recording('my_video.h264')
camera.wait_recording(60)
camera.stop_recording()
```

<br>

**포맷 조정**

picam_video_ex02.py

```python
from io import BytesIO
from picamera import PiCamera

stream = BytesIO()
camera = PiCamera()
camera.resolution = (640, 480)

camera.start_recording(stream, format='h264', quality=23)
camera.wait_recording(15)
camera.stop_recording()
```

-   bitrate
    -   default: 17000000 (17Mbps)
    -   maximum: 25000000 (25Mbps)
-   quality
    -   between 1 (highest quality) and 40 (lowest quality)
    -   20~25 적당

<br>

### 여러 파일로 녹화하기

-   split_recording('파일명')
    -   녹화 중 여러 파일에 저장하기
-   record_sequence(파일명 리스트)
    -   for 문의 시퀀스로 사용

<br>

**여러 파일에 저장하기**

picam_video_ex03.py

```python
from picamera import PiCamera

camera = PiCamera(resolution=(640, 480))
camera.start_recording('1.h264')
camera.wait_recording(5)

for i in range(2, 11):
    camera.split_recording('%d.h264' % i)
    camera.wait_recording(5)
    
camera.stop_recording()
```

<br>

**여러 파일에 저장하기2**

picam_video_ex04.py

```python
from picamera import PiCamera

camera = PiCamera(resolution=(640, 480))

for filename in camera.record_sequence('%d.h264' % i for i in range(1, 11)):
	camera.wait_recording(5)
```

<br>

### 환형 스트림에 녹화하기

-   PiCameraCircularIO 클래스
    -   동작을 감지하고 동작이 감지 된 비디오 만 디스크에 기록하려는 보안 응용

<br>

**환형 스트림에 녹화하기**

picam_video_ex05.py

```python
import io
import random
from picamera import PiCamera, PiCameraCircularIO

def motion_detected():
    # Randomly return True (like a fake motion detection routine)
    return random.randint(0, 10) == 0

camera = PiCamera()
stream = PiCameraCircularIO(camera, seconds=20)

camera.start_recording(stream, format='h264')
try:
    while True:
        camera.wait_recording(1)
        if motion_detected():
            # 동작이 감지됬다면 10초간 녹화하여 디스크에 스트림을 기록
            camera.wait_recording(10)
            stream.copy_to('motion.h264') # 스트림을 파일로 저장하기
finally:
	camera.stop_recording()
```

<br>

**환형 스트림에 녹화하기 - 초음파 센서**

picam_video_ex05_2

```python
from gpiozero import DistanceSensor
import io
import random
from picamera import PiCamera, PiCameraCircularIO

sensor = DistanceSensor(23, 24)

def motion_detected():
    return sensor.distance <= 0.2

camera = PiCamera()
stream = PiCameraCircularIO(camera, seconds=20)

camera.start_recording(stream, format='h264')
try:
    while True:
        camera.wait_recording(1)
        if motion_detected():
            print('motion detected')
            camera.start_preview()
            # 동작이 감지됬다면 10초간 녹화하여 디스크에 스트림을 기록
            camera.wait_recording(10)
            camera.stop_preview()
            stream.copy_to('motion.h264') # 스트림을 파일로 저장하기
finally:
	camera.stop_recording()
```




# python-picamera 2 이미지 캡처

### 이미지 캡처(이미지 촬영)

-   `camera.capture('파일명' [, '포맷'])` # 저장할 파일 경로
-   `camera.capture(file [, '포맷'])` # 파일 객체
-   `camera.capture(stream [, '포맷'])` # IO.Bytes 스트림

<br>

 picam_capture_ex01.py

```python
from time import sleep
from picamera import PiCamera

camera = PiCamera()
camera.resolution = (1024, 768)
camera.start_preview()

# Camera warm-up time
sleep(2)
camera.capture('foo.jpg') # 저장할 파일명 지정, 파일 확장명으로 포맷 결정
```

<br>

### 스트림으로 캡쳐하기

-   스트림 객체
    -   socket() 객체
    -   io.BytesIO stream
    -   기존 열려있는 파일 객체 등

<br>

**스트림으로 캡처하기**

picam_capture_ex02.py

```python
from io import BytesIO
from time import sleep
from picamera import PiCamera

# Create an in-memory stream
my_stream = BytesIO()

camera = PiCamera()
camera.start_preview()
# Camera warm-up time
sleep(2)

camera.capture(my_stream, 'jpeg') # 포맷 지정 필요
```

<br>

**파일로 캡처하기**

picam_capture_ex03.py

```python
from time import sleep
from picamera import PiCamera

# Explicitly open a new file called my_image.jpg
my_file = open('my_image.jpg', 'wb')

camera = PiCamera()
camera.start_preview()
sleep(2)

camera.capture(my_file)
```

<br>

**PIL 객체로 캡처하기**

picam_capture_ex04.py

```python
from io import BytesIO
from time import sleep
from picamera import PiCamera
from PIL import Image

# Create the in-memory stream
stream = BytesIO()

camera = PiCamera()

camera.start_preview()
sleep(2)
camera.capture(stream, format='jpeg')

# 내용을 읽기위해 스트림을 되감기함(rewind)
stream.seek(0)
image = Image.open(stream)
```

<br>

**캡처 이미지 크기 조정**

picam_capture_ex05.py

```python
from time import sleep
from picamera import PiCamera

camera = PiCamera()
camera.resolution = (1024, 768)
camera.start_preview()

# Camera warm-up time
sleep(2)
camera.capture('foo.jpg', resize=(320, 240))
```

<br>

### 연속 사진 촬영

-   camera.capture_sequence(파일명 리스트(또는 튜플))
-   capture_continuous('파일명 패턴')
    -   for 루프의 시퀀스로 사용
    -   파일명 패턴
        -   'img{counter:03d}.jpg'
        -   'img{timestamp:%Y-%m-%d-%H-%M}.jpg'

<br>

**연속 이미지 캡처**

picam_capture_ex06.py

```python
from time import sleep
from picamera import PiCamera

camera = PiCamera(resolution=(1280, 720), framerate=30)

camera.iso = 100
sleep(2)

camera.shutter_speed = camera.exposure_speed
camera.exposure_mode = 'off'
g = camera.awb_gains
camera.awb_mode = 'off'
camera.awb_gains = g

# 고정된 설정으로 여러 사진 찍기
camera.capture_sequence(['image%02d.jpg' % i for i in range(10)])
```

<br>

**연속 이미지 캡처**

picam_capture_ex07.py

```python
from time import sleep
from picamera import PiCamera

camera = PiCamera()
camera.start_preview()
sleep(2)

for filename in camera.capture_continuous('img{counter:03d}.jpg'):
    print('Captured %s' % filename)
    sleep(10) # wait 10 seconds
```

<br>
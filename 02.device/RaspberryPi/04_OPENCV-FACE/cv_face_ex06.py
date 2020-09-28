import numpy as np
from cam import USBCam
import cv2

FACE_WIDTH = 200
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
ix = 0
def save_image(img):
    global ix
    cv2.imwrite(f'p:/workspace/04_OPENCV-FACE/face_{ix:04d}.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, 90])
    ix += 1

face_image = np.array((FACE_WIDTH, FACE_WIDTH,3), dtype=int)

def detect_face(frame):
    global face_image
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # 이미지에서 얼굴을 검출합니다.
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    
    # 얼굴이 검출되었다면 얼굴 위치에 대한 좌표 정보를 리턴받습니다.
    for (x,y,w,h) in faces:
        # 원본 이미지에 얼굴의 위치를 표시
        # cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        minLength = min(w, h)
        if minLength < 150: break
        width = max(w, h)

        # 얼굴 부분 검출
        # face_image = frame[y:y+h, x:x+w].copy()
        x = x + w//2 - width//2
        y = y + h//2 - width//2
        face_image = frame[y:y+width, x:x+width].copy()
        cv2.rectangle(frame,(x,y),(x+width,y+width),(255,0,0),2)

        face_image = cv2.resize(face_image, dsize=(FACE_WIDTH, FACE_WIDTH), interpolation=cv2.INTER_AREA)

        save_image(face_image) # 얼굴영역 저장
    
    frame[0:FACE_WIDTH, 0:FACE_WIDTH] = face_image[:] # 좌측 상단에 출력
    
    return True


c = USBCam(show = True)
print('cam start')
c.run(detect_face)
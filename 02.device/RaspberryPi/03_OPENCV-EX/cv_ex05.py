import cv2
# cap = cv2.VideoCapture('http://192.168.0.2:4747/video')  # droid cam
cap = cv2.VideoCapture('./data/vtest.avi')  # 비디오 파일 재생

frame_size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
              int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

print('frame_size = ', frame_size)

while True:
    retval, frame = cap.read()  # 프레임 캡처
    if not retval: break

    cv2.imshow('frame', frame)
    key = cv2.waitKey(40)  # 초당 25 frame
    if key == 27: break

if cap.isOpened():
    cap.release()

cv2.destroyAllWindows()

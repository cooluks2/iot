import cv2
import numpy as np

face_classifier = cv2.CascadeClassifier('haarcascade_fullbody.xml')

cap = cv2.VideoCapture('./data/vtest.avi')


while True:
    ret, frame = cap.read()
    if ret:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = face_classifier.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            cropped_face = frame[y:y+h, x:x+w].copy()
            cropped_face = cv2.resize(cropped_face, dsize=(300, 300),
                                    interpolation=cv2.INTER_AREA)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 3)
            
        cv2.imshow('video', frame)
        
        if cv2.waitKey(1) == 27: break  # ESC 키
    else: break

cap.release()
cv2.destroyAllWindows()

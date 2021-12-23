from typing import Any
import cv2

# 카메라 장치 열기
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print('Camera open failed')
    exit()



#동영상 촬영하기
while True:
    ret, frame = cap.read()
    if not ret:
        break
    edge = cv2.Canny(frame,50,100)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame', frame)
    cv2.imshow('edge',edge)
    cv2.imshow('gray',gray)
    
    if cv2.waitKey(1) == 13:
        break

cap.release()
cv2.destoryAllWindows()

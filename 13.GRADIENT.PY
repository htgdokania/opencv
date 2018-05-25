import cv2
import numpy as np

cap=cv2.VideoCapture(0)

while True:
    _,gray=cap.read()

    frame=cv2.cvtColor(gray,cv2.COLOR_BGR2GRAY)
    laplacion=cv2.Laplacian(frame,cv2.CV_64F)
    sobelx=cv2.Sobel(frame,cv2.CV_64F,1,0,ksize=5)
    sobely=cv2.Sobel(frame,cv2.CV_64F,0,1,ksize=5)
    

    cv2.imshow('original',frame)
    cv2.imshow('lap',laplacion)
    cv2.imshow('x',sobelx)
    cv2.imshow('y',sobely)
    

    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
cv2.destroyAllWindows()
cap.release()

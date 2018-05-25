import cv2
import numpy as np

cap=cv2.VideoCapture(0)

while True:
    _,frame=cap.read()

    laplacion=cv2.Laplacian(frame,cv2.CV_64F)
    sobelx=cv2.Sobel(frame,cv2.CV_64F,1,0,ksize=5)
    sobely=cv2.Sobel(frame,cv2.CV_64F,0,1,ksize=5)

    edges=cv2.Canny(frame,100,200)

    cv2.imshow('original',frame)
    cv2.imshow('lap',laplacion)
    cv2.imshow('x',sobelx)
    cv2.imshow('y',sobely)
    
    cv2.imshow('edge',edges)
    

    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
cv2.destroyAllWindows()
cap.release()

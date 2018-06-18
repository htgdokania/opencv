#code to show only red color  trial and error
import cv2
import numpy as np
cap=cv2.VideoCapture(0)

while True:
    _,frame=cap.read()
    #hue saturation value=HSV
    cv2.namedWindow('hsv',cv2.WINDOW_NORMAL)
    cv2.resizeWindow('hsv',100,100)
    cv2.namedWindow('frame',cv2.WINDOW_NORMAL)
    cv2.resizeWindow('frame',100,100)
    cv2.namedWindow('mask',cv2.WINDOW_NORMAL)
    cv2.resizeWindow('mask',100,100)
    cv2.namedWindow('res',cv2.WINDOW_NORMAL)
    cv2.resizeWindow('res',100,100)
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    cv2.imshow('hsv',hsv)
    low_red=np.array([150,150,50])
    up_red=np.array([255,255,255])

    mask=cv2.inRange(hsv,low_red,up_red)
    result=cv2.bitwise_and(frame,frame,mask=mask)

    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',result)

    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
cv2.destroyAllWindows()
cap.release()

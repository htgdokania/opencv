#code to show only red color  trial and error
import cv2
import numpy as np
cap=cv2.VideoCapture(0)

while True:
    _,frame=cap.read()
    #hue saturation value=HSV
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    cv2.imshow('hsv',hsv)
    low_red=np.array([150,150,50])
    up_red=np.array([255,255,255])

    mask=cv2.inRange(hsv,low_red,up_red)
    mask_inv=cv2.bitwise_not(mask)
    result=cv2.bitwise_and(frame,frame,mask=mask_inv)

    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',result)

    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
cv2.destroyAllWindows()
cap.release()

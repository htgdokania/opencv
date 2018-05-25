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
    
    kernel=np.ones((15,15),np.float32)/225
    
    smooth1=cv2.filter2D(mask_inv,-1,kernel)
    smooth2=cv2.filter2D(mask,-1,kernel)
    result=cv2.bitwise_and(frame,frame,mask=smooth2)

    smooth=cv2.filter2D(result,-1,kernel)
    
    blur=cv2.GaussianBlur(result,(15,15),0)
    median=cv2.medianBlur(result,15)

    cv2.imshow('blur',blur)
    cv2.imshow('smooth',smooth)
    cv2.imshow('median',median)
   
    # cv2.imshow('frame',frame)
    # cv2.imshow('mask',mask)
    cv2.imshow('res',result)

    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
cv2.destroyAllWindows()
cap.release()

import cv2
import numpy as np

img=cv2.imread('1')
cv2.imshow('img',img)
imggray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

tem=cv2.imread('temp.png',0)
cv2.imshow('e',tem)
w,h=tem.shape

res=cv2.matchTemplate(imggray,tem,cv2.TM_CCOEFF_NORMED)
cv2.imshow('res',res)
threshhold=0.8

loc=np.where(res>=threshhold)

for pt in zip(*loc[::-1]):
    cv2.rectangle(img,pt,(pt[0]+w,pt[1]+h),(0,255,255),2)

cv2.imshow('detected',img)

cv2.waitKey(0)
cv2.destroyAllWindows()

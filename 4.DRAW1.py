import numpy as np
import cv2

img=cv2.imread('watch.png',cv2.IMREAD_COLOR)

cv2.line(img,(0,0),(150,150),(0,100,255),15)
cv2.rectangle(img,(15,25),(200,200),(0,255,0),5)
cv2.circle(img,(100,63),55,(255,100,0),-1)
pts=np.array([[15,25],[200,200],[70,20],[50,10]],np.int32)
cv2.polylines(img,[pts],False,(255,255,0),10)

font =cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'openCV Tuts!',(0,300),font,2,(200,55,88),5,cv2.LINE_AA)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

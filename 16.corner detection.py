import cv2
import numpy as np

img=cv2.imread('corner',1)
gray=cv2.imread('corner',0)
gray=np.float32(gray)


corners = cv2.goodFeaturesToTrack(gray,2000,0.1,10,useHarrisDetector=True)
corners=np.int0(corners)

for corner in corners:
    x,y=corner.ravel()
    cv2.circle(img,(x,y),3,255,-1)

cv2.imshow('corners',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

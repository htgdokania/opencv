import cv2
img1=cv2.imread('three.png',1)
img2=cv2.imread('four.png',1)

add=cv2.addWeighted(img1,0.6,img2,0.4,0)
cv2 .imshow('add',add)
cv2.waitKey(0)
cv2.destroyAllWindows()

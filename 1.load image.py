#load image watch named image.jpg and display using cv2 library

import cv2

img = cv2.imread('1',)
img2= cv2.imread('image.jpg',cv2.IMREAD_GRAYSCALE)

cv2.imshow('image', img)
#print ('press any key to continue')
#cv2.waitKey()
cv2.imshow('image1', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

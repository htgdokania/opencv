import numpy
import cv2
import matplotlib as plt

img =cv2.imread('image.jpg',cv2.IMREAD_GRAYSCALE)
#IMREAD_COLOR=1
#IMREAD_UNCHANGED=-1

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2

img=cv2.imread('1',1)

crop=img[14:41,93:106]
cv2.imwrite('template.png',crop)

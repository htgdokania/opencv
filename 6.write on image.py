import cv2
img=cv2.imread('1',1)
cv2.imshow('img',img)
cv2.line(img,(0,0),(274,181),(255,255,255),15)
cv2.imshow('img1',img)
font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'HTG',(2,182),font,1,(255,255,0),3)
cv2.imshow('img2',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

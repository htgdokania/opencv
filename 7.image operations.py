import cv2
img=cv2.imread('1',1)
x=0
while(x<180):
    img[0+x,0+x]=[255,255,255]
    img[180-x,0+x]=[255,255,255]
    cv2.imshow('img2',img)
    x+=1
    cv2.waitKey(0)

img[100:150,100:160]=img[120:170,0:60]
cv2.imshow('img3',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
              

















































































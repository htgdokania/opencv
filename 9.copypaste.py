import cv2
img1=cv2.imread('11',1)
img=cv2.imread('logopython',1)
x=0
y=0
rows,cols,channels=img.shape
while(y<=200):
    img1[x,y]=img[x,y]
    x+=1
    y+=1
cv2.imshow('new',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2
img=cv2.imread('logopython',1)
r,c,ch=img.shape
for i in range(r):
    for j in range(c):
        if(a.any(img[i,j])==255):
            img[i,j]=[0,0,0]
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

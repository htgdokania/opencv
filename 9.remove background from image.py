import cv2
img1=cv2.imread('11',1)
r,c,ch=img1.shape
#cv2.rectangle(img1,(0,0),(c,r),(0,255,0),-1)
img=cv2.imread('logopython',1)
cv2.imshow('img',img)
print(img[100,100])
rows,cols,channels=img.shape
print(rows)
print(cols)
imggray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,mask =cv2.threshold(imggray,220,255,cv2.THRESH_BINARY_INV)
print(mask[100,100])
cv2.imshow('mask',mask)
mask_inv=cv2.bitwise_not(mask)
cv2.imshow('mask_inv',mask_inv)
print(mask_inv)

for i in range(0,cols):
    for j in range(0,rows):
        if(mask_inv[i,j]==0):
            img1[i+50,j+50]=img[i,j]
         


cv2.imshow('newim',img1)

cv2.waitKey(0)
cv2.destroyAllWindows()

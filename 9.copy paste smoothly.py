import cv2
img1=cv2.imread('11',1)
img2=cv2.imread('logopython',1)
rows,cols,channels=img2.shape
roi=img1[0:rows,0:cols]
imggray=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
ret,mask =cv2.threshold(imggray,220,255,cv2.THRESH_BINARY_INV)
mask_inv=cv2.bitwise_not(mask)
img_bg=cv2.bitwise_and(roi,roi,mask=mask_inv)
cv2.imshow('img_bg',img_bg)
img_fg=cv2.bitwise_and(img2,img2,mask=mask)

cv2.imshow('img_fg',img_fg)
dst=cv2.add(img_bg,img_fg)
cv2.imshow('pre',dst)
img1[0:rows,0:cols]=dst
cv2.imshow('final',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()

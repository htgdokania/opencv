import cv2

img=(255,0,255,0,0,0,255)
#img=[[255,0,255,0,0,0],[255,0,255,0,0,0],[255,0,255,0,0,0]]
#the above comment line is not working
cv2.imshow('htg',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

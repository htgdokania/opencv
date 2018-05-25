import numpy as np
import cv2
cap=cv2.VideoCapture('Anniversary.mp4')

while (1):
    ret,frame=cap.read()
    cv2.imshow('frame',frame)
    if cv2.waitKey(25) & 0xFF==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

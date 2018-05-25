#code not working what is the issue??

import cv2
import numpy as np

cap=cv2.VideoCapture(0)
fourcc=cv2.VideoWriter_fourcc(*'divx')
out=cv2.VideoWriter('gray.mp4',fourcc,30.0,(640,480))

while True:
    ret,frame=cap.read()
    gray= cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    out.write(gray)
    cv2.imshow('gray',gray)
    if cv2.waitKey(25) & 0xFF==ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()

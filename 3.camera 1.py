import cv2
import numpy as np

cap=cv2.VideoCapture(0)
#fourcc=cv2.VideoWriter_fourcc(*'divx')
#fourcc = cv2.cv.CV_FOURCC(*'XVID')
#out1=cv2.VideoWriter('output.mp4',fourcc,30.0,(160,120))

#out=cv2.VideoWriter('output1.mp4',fourcc,30.0,(640,480))

while True:
    
    ret,frame=cap.read()
 #   gray= cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
  #  out.write(gray)
#    out1.write(frame)
    cv2.namedWindow('frame',cv2.WINDOW_NORMAL)
    cv2.resizeWindow('frame', 640,480)
    cv2.imshow('frame',frame)

    if cv2.waitKey(25) & 0xFF==ord('q'):
        break

cap.release()
#out.release()
#out1.release()
cv2.destroyAllWindows()

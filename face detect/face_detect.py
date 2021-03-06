#htg
import cv2

#load cascade xml files
face_cascade= cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#capture video frame by frame
cap=cv2.VideoCapture(0)

while True:
    ret,frame=cap.read()
    cv2.namedWindow('frame',cv2.WINDOW_NORMAL)
    cv2.resizeWindow('frame', 160,120)
    frame=cv2.flip(frame,0)
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)#convert current frame to gray 

    #detect face coordinates x,y,w,h
    faces=face_cascade.detectMultiScale(gray,1.3,5)
    c=0
    for(x,y,w,h) in faces:
        frame=cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),6)# frame,coordinates, color,thickness
        c+=1
    cv2.imshow('frame',frame) #display image frame by frame
    print(c)
    if cv2.waitKey(25)==ord('q'):
        break

cv2.destroyAllWindows()

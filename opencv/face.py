import cv2 as cv 
import numpy as np 

face_cascade=cv.CascadeClassifier('haarcascade_frontalface_default.xml')
cap=cv.VideoCapture(0)
while cap.isOpened() :
    _,img=cap.read()
    gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    gray1=gray[200:500,200:500]
    cv.rectangle(img,(200,200),(500,500),(0,255,0),2)
    faces=face_cascade.detectMultiScale(gray1,2,4)

    for (x,y,w,h) in faces :
        cv.rectangle(img,(x+200,y+200),(x+w+200,y+h+200),(0,0,255),3)


    cv.imshow("imh",img)
    if cv.waitKey(1) & 0xFF == ord('q') :
        break




cap.release()

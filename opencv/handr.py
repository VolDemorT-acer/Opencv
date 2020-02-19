import cv2 as cv 
import numpy as np 


cap=cv.VideoCapture(0)

#loading haar cascades
palm_cascade=cv.CascadeClassifier('opencv\palm_v4.xml')
close_cascade=cv.CascadeClassifier('opencv\closed_frontal_palm.xml')
left_cascade=cv.CascadeClassifier(r'opencv\xml\left.xml')
right_cascade=cv.CascadeClassifier(r'opencv\xml\right.xml')

gest_cascade=cv.CascadeClassifier(r'opencv\xml\aGest.xml')



while cap.isOpened() :
    _,img=cap.read()
    
    gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    gray1=gray[150:400,30:300]
    cv.rectangle(img,(30,150),(300,400),(0,255,0),2)

    #cascade detection
    palms= palm_cascade.detectMultiScale(gray1, 1.1, 4,0|cv.CASCADE_SCALE_IMAGE,minSize=(20,20))
    closes= close_cascade.detectMultiScale(gray1, 1.1, 4,0|cv.CASCADE_SCALE_IMAGE,minSize=(20,20))
    lefts= left_cascade.detectMultiScale(gray1, 1.1, 2,0|cv.CASCADE_SCALE_IMAGE,minSize=(20,20))
    rights= right_cascade.detectMultiScale(gray1, 1.1, 1,0|cv.CASCADE_SCALE_IMAGE,minSize=(20,20))
    fingers= gest_cascade.detectMultiScale(gray1, 1.1, 1,0|cv.CASCADE_SCALE_IMAGE,minSize=(20,20))
    

    
    #gesturechoosing statements ahead
    detected=False
    
    for palm in palms :
        x,y,w,h=palm
        print("palm")
        cv.putText(img,'PALM',(25,100),cv.FONT_HERSHEY_COMPLEX,2,(0,255,0),4)
        cv.rectangle(img,(x+30,y+150),(x+w+30,y+h+150),(0,0,255),3)
        detected=True
    if(not detected):
       for close in closes :
          x1,y1,w1,h1=close
          print("close palm")
          cv.putText(img,'FIST',(25,100),cv.FONT_HERSHEY_COMPLEX,2,(0,255,0),4)
          cv.rectangle(img,(x1+30,y1+150),(x1+w1+30,y1+h1+150),(0,0,255),3)
          detected=True
    if(not detected) :
       for left in lefts :
          x3,y3,w3,h3=left
          cv.putText(img,'LEFTSIDE',(25,100),cv.FONT_HERSHEY_COMPLEX,2,(0,255,0),4)
          print("left")
          cv.rectangle(img,(x3+30,y3+150),(x3+w3+30,y3+h3+150),(0,0,255),3)
          detected=True
    if(not detected):
       for right in rights :
           x5,y5,w5,h5=right
           cv.putText(img,'RIGHTSIDE',(25,100),cv.FONT_HERSHEY_COMPLEX,2,(0,255,0),4)
           print("right")
           cv.rectangle(img,(x5+30,y5+150),(x5+w5+30,y5+h5+150),(0,0,255),3)
    if(not detected):
        for finger in fingers:
           x7,y7,w7,h7=finger
           cv.putText(img,'Finger',(25,100),cv.FONT_HERSHEY_COMPLEX,2,(0,255,0),4)
           print("Finger")
           cv.rectangle(img,(x7+30,y7+150),(x7+w7+30,y7+h7+150),(0,0,255),3)


    cv.imshow("FinalFrame",img)
    if cv.waitKey(160) & 0xFF == ord('q') :
        break
cv.destroyAllWindows()
cap.release()



#rpalm_cascade=cv.CascadeClassifier(r'opencv\xml\rpalm.xml')
#face_cascade=cv.CascadeClassifier('opencv\palm_v4.xml')
#palms = palm_cascade.detectMultiScale(img, 1.1, detect_neighbor,0|cv2.CASCADE_SCALE_IMAGE,minSize=(20,20))
#for rpalm in rpalms :
        #x6,y6,w6,h6=rpalm
        #print("rplam")
        #cv.rectangle(img,(x6+200,y6+200),(x6+w6+200,y6+h6+200),(0,0,255),3)

#rpalms= rpalm_cascade.detectMultiScale(gray1, 1.1, 4,0|cv.CASCADE_SCALE_IMAGE,minSize=(20,20))
 ##for finger in fingers:
           #x7,y7,w7,h7=finger
           #cv.putText(img,'Finger',(25,100),cv.FONT_HERSHEY_COMPLEX,2,(0,255,0),4)
           #print("Finger")
           #cv.rectangle(img,(x7+30,y7+150),(x7+w7+30,y7+h7+150),(0,0,255),3)

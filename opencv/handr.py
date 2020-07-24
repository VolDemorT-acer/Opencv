import cv2 as cv 
import numpy as np 
from time import time 
import pyautogui as py 
#from datetime import datetime

cap=cv.VideoCapture(0)

#loading haar cascades
palm_cascade=cv.CascadeClassifier('opencv\palm_v4.xml')
close_cascade=cv.CascadeClassifier(r'opencv\fist.xml')
left_cascade=cv.CascadeClassifier(r'opencv\xml\left.xml')
right_cascade=cv.CascadeClassifier(r'opencv\xml\right.xml')
#gest_cascade=cv.CascadeClassifier(r'opencv\xml\aGest.xml')
times=[]
position_array=[]
velsy=[]
velsx=[]
scrolling=True 
while cap.isOpened() :
    _,img=cap.read()
    
    gray1=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    gray=cv.threshold(gray1,120,200,cv.THRESH_BINARY)
    gray1= cv.GaussianBlur(gray1,(3,3),1)
   
    cv.imshow("thresh",gray1)
    cv.rectangle(img,(30,150),(300,400),(0,255,0),2)

    #cascade detection
    palms= palm_cascade.detectMultiScale(gray1, 1.1, 4,0|cv.CASCADE_SCALE_IMAGE,minSize=(20,20))
    closes= close_cascade.detectMultiScale(gray1, 1.1, 4,0|cv.CASCADE_SCALE_IMAGE,minSize=(20,20))
    lefts= left_cascade.detectMultiScale(gray1, 1.1, 2,0|cv.CASCADE_SCALE_IMAGE,minSize=(20,20))
    rights= right_cascade.detectMultiScale(gray1, 1.1, 1,0|cv.CASCADE_SCALE_IMAGE,minSize=(20,20))
    #$fingers= gest_cascade.detectMultiScale(gray1, 1.1, 1,0|cv.CASCADE_SCALE_IMAGE,minSize=(20,20))
    

    
    #gesturechoosing statements ahead
    detected=False
    
    
    
    #t=time.time()
    #seconds=[0]
    if len(palms)==0 :
            position_array=[]
            times=[]
            velsy=[]
            velsx=[]
          
    detected=False

    if(not detected)  :
            for left in lefts :
                  
                    detected=True
                    print("left")
                    w1,h1 =py.size()
                    
                        
                    #py.moveRel(50,0,py.easeInCirc(0.1))
                    x1,y1=py.position()
                    if w1-x1>50 :
                             py.moveRel(50,0,py.easeInCirc(.5))
                    else :
                             py.moveTo(50,y1,py.easeInCirc(0.1))

                        
    if(not detected) :
      for palm in palms :
        x,y,w,h=palm
        print("palm")
        t=time()
        times.append(t)
        

        position_array.append((x+w/2,y+h/2))
        if len(times)>=2 and len(position_array)>=2 :
                if ((position_array[-1][1]-position_array[-2][1])>=10 or (position_array[-1][1]-position_array[-2][1])<=-10) and (times[-2]!=times[-1]):
                        vel_nowy=(position_array[-1][1]-position_array[-2][1])/(times[-2]-times[-1])
                        vel_nowx=(position_array[-1][0]-position_array[-2][0])/(times[-2]-times[-1])
                        
                        if vel_nowy<=10 and vel_nowy>=-10 :
                              vel_nowy=0
                        if vel_nowx<=10 and vel_nowx>=-10 :
                              vel_nowx=0
                                            
                        velsy.append(vel_nowy) 
                        velsx.append(vel_nowx)
                        
                        k=1
                
                        if len(velsy)>=1 :
                            vy=0
                            if velsy[-1]< 0: 
                                
                                for i in range(len(velsy)) :
                                        if velsy[len(velsy)-i-1]<0 :
                                               k=k+1
                                               vy+=velsy[len(velsy)-i-1]
                                        else :
                                                break 
                                        
                                vy/=k
                            elif velsy[-1]> 0:
                        
                                for i in range(len(velsy)) :
                                        if velsy[len(velsy)-i-1]>0 :
                                               k=k+1
                                               vy+=velsy[len(velsy)-i-1]
                                        else :
                                                break 
                                        
                                vy/=k
                        if len(velsx)>=1 :
                            vx=0
                            if velsx[-1]< 0: 
                                
                                for i in range(len(velsx)) :
                                        if velsx[len(velsx)-i-1]<0 :
                                               k=k+1
                                               vy+=velsx[len(velsx)-i-1]
                                        else :
                                                break 
                                        
                                vx/=k
                            elif velsx[-1]> 0:
                        
                                for i in range(len(velsx)) :
                                        if velsy[len(velsx)-i-1]>0 :
                                               k=k+1
                                               vx+=velsy[len(velsx)-i-1]
                                        else :
                                                break 
                                        
                                vx/=k
                        
                        print(vy)
                        if ((position_array[-1][0]-position_array[-2][0])>=10 or (position_array[-1][0]-position_array[-2][0])<=-10) and (times[-2]!=times[-1]):
                                w1,h1 =py.size()
                                vel_nowx=(position_array[-1][0]-position_array[-2][0])/(times[-2]-times[-1])
                    
                        
                    #py.moveRel(50,0,py.easeInCirc(0.1))
                                x1,y1=py.position()
                                
                                if w1-x1>50 :
                                        py.moveRel(vel_nowx*1,0,py.easeInCirc(.5))
                                else :
                                        py.moveTo(50,y1,py.easeInCirc(0.1))

                            
                        py.scroll(int(vy)*5)

                        

                        #if py.scroll(int(vy)*6) is None :
                        
                         
        times.append(t)
        detected=True

    if(not detected) :

        for close in closes:
             x1,y1,w1,h1 =close 
             py.click()
             print("click")
             detected=True

    

            
        
        
    
        #cv.putText(img,'{},{},{}'.format(x+h/2,y+w/2,t),(25,100),cv.FONT_HERSHEY_COMPLEX,2,(0,255,0),4)
        #cv.rectangle(

        
    
    
    

    cv.imshow("FinalFrame",img)
    if cv.waitKey(10) & 0xFF == ord('q') :
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

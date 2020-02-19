import cv2 as cv 

cap=cv.VideoCapture('opencv\vtest.avi')
#ret,frame2=cap.read() 
ret,frame1=cap.read()


while cap.isOpened() :
    # diff=cv.absdiff(frame1,frame2)
    # gray=cv.cvtColor(diff,cv.COLOR_BGR2GRAY)
    
    # blur=cv.GaussianBlur(gray,(5,5),0)
    # _,thresh=cv.threshold(blur,20,255,cv.THRESH_BINARY)
    # dilated=cv.dilate(blur,None,iterations=3)
    # contours,heirachy=cv.findContours(dilated,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)

    # for contour in contours :
    #    ( x,y,w,h) =cv.boundingRect(contour)

    #    if cv.contourArea(contour)<=1000  :
    #        continue 
    #    else :
    #         cv.rectangle(frame1,(x,y),(x+w,y+h),(0,255,0),2)
    #         cv.putText(frame1,"Status:{}".format('Movement'),(10,20),cv.FONT_HERSHEY_SCRIPT_COMPLEX,1,(0,0,255),3)

    
    

    cv.imshow('feed',frame1)
    #frame1=frame2
    #ret,frame2=cap.read()

    if cv.waitKey(1) & 0xFF==ord('q') :
        break

cap.release()
cv.destroyAllWindows()

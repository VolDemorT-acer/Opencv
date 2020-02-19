import cv2 as cv 


img= cv.imread("opencv\pic2.png")

img_gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
_,thresh=cv.threshold(img_gray,240,255,cv.THRESH_BINARY)
contours,_ =cv.findContours(thresh,cv.RETR_TREE,cv.CHAIN_APPROX_NONE)

for contour in contours :
   approx = cv.approxPolyDP(contour,0.01*cv.arcLength(contour,True),True)
   cv.drawContours(img,[approx],0,(0,0,255),2)
   x=approx.ravel()[0]
   y=approx.ravel()[1]

   if len(approx)==3 :
        cv.putText(img,"Triangle",(x,y),cv.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),1)
   elif len(approx)==4 :
        (x1,y1,w,h)=cv.boundingRect(approx)
        aspectratio=float(w)/h
        if aspectratio>=0.95 and aspectratio<=1.05 :
              cv.putText(img,"Square",(x,y),cv.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),1)
        else :
            
            cv.putText(img,"Rect",(x,y),cv.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),1)   


   elif len(approx)==5 :
        cv.putText(img,"Pentagon",(x,y),cv.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),1)   
   elif len(approx)==10:
        cv.putText(img,"Square",(x,y),cv.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),1)   

   else :
       cv.putText(img,"Circle",(x,y),cv.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),1) 



cv.imshow("t",img)
cv.waitKey(0)
cv.destroyAllWindows()

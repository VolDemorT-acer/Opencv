import cv2 as cv 
import numpy as np 
from matplotlib import pyplot as plt 

img=cv.imread("opencv\smarties.png")
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
gray=cv.medianBlur(gray,5)
circles=cv.HoughCircles(gray,cv.HOUGH_GRADIENT,1,20,param1=50,param2=30,minRadius=0,maxRadius=0)
detected_circles=np.uint16(np.around(circles))
for (x,y,r) in detected_circles[0,:] :
    cv.circle(img,(x,y),r,(0,255,0),3)
    cv.circle(img,(x,y),2,(255,0,0),1)
cv.imshow("output",img)

cv.waitKey(0)
cv.destroyAllWindows()
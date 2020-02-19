import cv2 as cv
import numpy as np 

#diff than global thrsh here we are thrshing for specific parts

img=cv.imread("opencv\lena.jpg",0)
_,th1=cv.threshold(img,127,255,cv.THRESH_BINARY)
th2=cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,2)
#mean of bksize*bksize neighbourhood o fx,y minus C
cv.imshow("IMage",img)
cv.imshow("th1",th1)
cv.imshow("th2",th2)

th3=cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,2)
#weightedmean of bksize*bksize neighbourhood o fx,y minus C

cv.imshow("th3",th3)


cv.waitKey(0)
cv.destroyAllWindows()
import cv2 as cv 
import numpy as np #threshlod value 


img=cv.imread('opencv\gradient.png',0)
_,th1=cv.threshold(img,50,255,cv.THRESH_BINARY)
cv.imshow("th1",th1)
_,th2=cv.threshold(img,200,255,cv.THRESH_BINARY_INV)
cv.imshow("th2",th2)
_,th3=cv.threshold(img,127,255,cv.THRESH_TRUNC)
cv.imshow("th3",th3)
_,th4=cv.threshold(img,127,255,cv.THRESH_TOZERO)
cv.imshow("th4",th4)
_,th5=cv.threshold(img,127,255,cv.THRESH_TOZERO_INV)
cv.imshow("th5",th5)



cv.imshow("Image",img)


cv.waitKey(0)
cv.destroyAllWindows()


#this is global threshholding that is for the all pixels oin img
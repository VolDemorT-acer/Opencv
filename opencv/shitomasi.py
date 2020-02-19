import cv2 as cv 
import numpy as np 
#improvement in haris

img=cv.imread("opencv\pic1.png")
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

corner=cv.goodFeaturesToTrack(gray,50,0.01,10
)
corner=np.int0(corner)

for i in corner :
     x,y =i.ravel()
     cv.circle(img,(x,y),3,255,-1)


cv.imshow("img",img)
if cv.waitKey(0) & 0xFF ==27 :
    cv.destroyAllWindows()
import cv2 as cv
import numpy as np 
from matplotlib import pyplot as plt 
img1=cv.imread("opencv\lena.jpg")
img =np.zeros((200,200),np.uint8)
cv.rectangle(img,(0,50),(100,200),(127),-1)
b,g,r=cv.split(img1)


#using matplt
hist=cv.calcHist([img1],[0],None,[256],[0,256])
plt.plot(hist)
plt.hist(img1.ravel(),256,[0,256])
plt.hist(b.ravel(),256,[0,256])
plt.hist(g.ravel(),256,[0,256])
plt.hist(r.ravel(),256,[0,256])
plt.show()
cv.imshow("img",img1)
cv.waitKey(0)
cv.destroyAllWindows()

import cv2 as cv
import numpy as np 
from matplotlib import pyplot  as plt


#cv.imshow("image",img)
#img=cv.cvtColor(img,cv.COLOR_BGR2RGB)

#plt.imshow(img)
#plt.xticks([]),plt.yticks([])
#plt.show()



#showing images in plt



img2=cv.imread('opencv\gradient.png',0)
_,th1=cv.threshold(img2,50,255,cv.THRESH_BINARY)

_,th2=cv.threshold(img2,200,255,cv.THRESH_BINARY_INV)

_,th3=cv.threshold(img2,127,255,cv.THRESH_TRUNC)

_,th4=cv.threshold(img2,127,255,cv.THRESH_TOZERO)

_,th5=cv.threshold(img2,127,255,cv.THRESH_TOZERO_INV)




titles=['orig','Bin','Bininv','trunc','tozer','tozerinv']
images=[img2,th1,th2,th3,th4,th5]


for i in range(6) :
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()
    


















#cv.waitKey(0)
#cv.destroyAllWindows()
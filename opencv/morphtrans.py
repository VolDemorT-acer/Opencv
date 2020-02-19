import cv2 as cv 
import numpy as np 
from matplotlib import pyplot as plt 

img = cv.imread("opencv\smarties.png",cv.IMREAD_GRAYSCALE)
_,mask=cv.threshold(img,220,255,cv.THRESH_BINARY_INV)
kernel=np.ones((3,3),np.uint8)
dilation=cv.dilate(mask,kernel,iterations=4)

erosion=cv.erode(mask,kernel,iterations=5)
opening=cv.morphologyEx(mask,cv.MORPH_OPEN,kernel)
closing=cv.morphologyEx(mask,cv.MORPH_CLOSE,kernel)

#kernel is square 
titles=['image','mask','dilation','erosion','opening','closing']
images=[img,mask,dilation,erosion,opening,closing]

for i in range(6) :
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()

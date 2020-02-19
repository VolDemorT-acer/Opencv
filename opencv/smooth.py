import cv2 as cv 
import numpy as np
from matplotlib import pyplot as plt 




img=cv.imread("opencv\lena.jpg")
img=cv.cvtColor(img,cv.COLOR_BGR2RGB)
kernel=np.ones((5,5),np.float32)/25

blur =cv.blur(img,(5,5))
dst=cv.filter2D(img,-1,kernel)
gblur=cv.GaussianBlur(img,(5,5),0)
mblur=cv.medianBlur(img,5)
bilateral=cv.bilateralFilter(img,9,75,75)




titles=['image','2d','blur','gblur','mblur','bilateral']
images=[img,dst,blur,gblur,mblur,bilateral]

for i in range(6) :
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()

#high pass filter for edge traicng
#low pass for smooting

#gaussian wt algo uses diff weight kernel in x and y that is we get hihher wt in  middle
#bilateral noise for less smoothening of images 
# median filter replaces with median with neighbouring pixels used for salt paper noise  

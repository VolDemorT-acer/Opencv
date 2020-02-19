import cv2 as cv 
import numpy as np 
from matplotlib import pyplot as plt 
def region_of_interest(img,vertices) :
    mask=np.zeros_like(img)
    #channel_count=img.shape[2]
    match_mask_color=255
    cv.fillPoly(mask,vertices,match_mask_color)
    masked_image=cv.bitwise_and(img,mask)
    return masked_image

img = cv.imread("opencv\Road.png")
img=cv.cvtColor(img,cv.COLOR_BGR2RGB)
print(img.shape)
height=img.shape[0]
width=img.shape[1]

refion_of_interest_vertices=[
    (0,height),(0,height/2),
    (width/2,10),(width,height/2),
    (width,height)
]
gry_img=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
canny=cv.Canny(gry_img,100,200)
cropped_image=region_of_interest(canny,np.array([refion_of_interest_vertices],np.int32))

lines=cv.HoughLinesP(cropped_image,6,np.pi/60,160,lines=np.array([]),minLineLength=40,maxLineGap=25)

def drawlines(img,lines) :
    img=np.copy(img)
    line_image=np.zeros((img.shape[0],img.shape[1],3),np.uint8)

    for line in lines :
        for x1,y1,x2,y2 in line :
            cv.line(line_image,(x1,y1),(x2,y2),(255,0,0),2)


    new=cv.addWeighted(img,0.6,line_image,1,0.0)
    return new


image_lines=drawlines(img,lines)  
plt.imshow(image_lines)
plt.show()
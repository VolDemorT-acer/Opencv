import cv2 as cv 
import numpy as np

images= [
r"C:\Users\VOLDERMORT\Documents\GitHub\Opencv\AntahsagriCourse\Assigment1\1.jpg",r'C:\Users\VOLDERMORT\Documents\GitHub\Opencv\AntahsagriCourse\Assigment1\2.jpg',
r'C:\Users\VOLDERMORT\Documents\GitHub\Opencv\AntahsagriCourse\Assigment1\3.jpg',r'C:\Users\VOLDERMORT\Documents\GitHub\Opencv\AntahsagriCourse\Assigment1\4.jpg',
r'C:\Users\VOLDERMORT\Documents\GitHub\Opencv\AntahsagriCourse\Assigment1\5.jpg',r'C:\Users\VOLDERMORT\Documents\GitHub\Opencv\AntahsagriCourse\Assigment1\6.jpg'
]

#read images
image1=cv.imread(images[0])
image2=cv.imread(images[1])
image3=cv.imread(images[2])
image4=cv.imread(images[3])
image5=cv.imread(images[4])
image6=cv.imread(images[5])




clahe= cv.createCLAHE(clipLimit=1.0,tileGridSize=(6,6))

def apply_brightness_contrast(image,contrast = 0,brightness=0) :
    if brightness!=0 :
        if brightness>0 :
          shadow= brightness 
          highlight= 255
        else :
           shadow=0 
           highlight=255+brightness
        alpha_b=(highlight-shadow)/255
        beta_b=shadow

        buf=cv.addWeighted(image,alpha_b,image,0,beta_b)
    else :
        buf=image.copy()

    if contrast!=0:
        f = float(131*(127+contrast)/(131-contrast)/127)
        aplha = f 
        beta = 127*(1-f)
        buf = cv.addWeighted(image,aplha,image,0,beta)
    return buf 


def clahe_contrast(image) :
    l,a,b= cv.split(cv.cvtColor(image,cv.COLOR_BGR2HSV))
    cl= clahe.apply(a) 
    res= cv.merge((l,cl,b))
    res=cv.cvtColor(res,cv.COLOR_HSV2BGR)
    return res

def scaleConversion(image) :
    alow = image.min()
    ahigh= image.max()
    amax=255
    amin=0
    alpha=amax/(ahigh-alow)
    beta=amin-alow*alpha
    adjusted = cv.convertScaleAbs(image,alpha=alpha,beta=beta)
    return adjusted

def hsv_contrast(image) :
    im= cv.cvtColor(image,cv.COLOR_BGR2HSV)
    im[:,:,2]=[[max(pixel-25,0) if pixel<190 else min(pixel+25,255) for pixel in row] for row in im[:,:,2]]
    im= cv.cvtColor(image,cv.COLOR_HSV2BGR)
    return im



imagearr=[image1,image2,image3,image4,image5,image6]

for i in range(6) :
        imagearr[i]=cv.resize(imagearr[i],(600,330))
        imagearr[i]=cv.GaussianBlur(imagearr[i],(3,3),1,imagearr[i],1)


        #applying contrast
        res=apply_brightness_contrast(imagearr[i],50, -100) #overall better just problems with sun
        # res=scaleConversion(imagearr[i])  #better  but not that much good with sun in background almost similar to first one
        # cv.imwrite(r"C:\Users\VOLDERMORT\Documents\GitHub\Opencv\AntahsagriCourse\Blur\{}.jpg".format(i+1),imagearr[i])

        res= np.hstack((res,imagearr[i]))
        cv.imshow("res{}".format(i),res)
        





cv.waitKey(0) 
cv.destroyAllWindows()
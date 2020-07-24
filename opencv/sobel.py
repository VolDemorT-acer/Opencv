import cv2 as cv
import numpy as np
import imutils



cap = cv.VideoCapture(0)
bgsustractor= cv.BackgroundSubtractorMOG2()
frames = 40



def thresholding_image(img,thresh_lower,thresh_higher) :
    pass 
    
def substracting_background(image) :
    pass

def processing_frame(image) :
    pass








while(cap.isOpened()) :
    _,frame= cap.read()
    frame = imutils.resize(frame, width=1000)
    frame=processing_frame(frame) 
    frame= substracting_background(frame)

    


    key =cv.waitKey(10)
    if key==



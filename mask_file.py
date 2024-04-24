import cv2
import numpy as np


def mask_generator(lh,ls,lv,uh,us,uv,hsv_img):
    l_value=np.array([73,115,100])###[69,131,100]80,90,85
    u_value=np.array([175,255,255])##[179,255,255]175,255,255
    
    
    mask=cv2.inRange(hsv_img,l_value,u_value)
    kernel=np.ones((5,5),np.uint8)
    cv2.erode(mask,kernel,iterations=1)
    cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel)
    cv2.dilate(mask,kernel,iterations=1)

    return mask

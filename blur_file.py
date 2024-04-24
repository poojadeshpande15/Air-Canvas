import cv2
import numpy

def blur(img):
    blur_img=cv2.GaussianBlur(img,(11,11),0)
    return blur_img

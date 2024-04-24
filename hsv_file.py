import cv2

def hsv(blur_img):
    hsv_img=cv2.cvtColor(blur_img,cv2.COLOR_BGR2HSV)
    return hsv_img

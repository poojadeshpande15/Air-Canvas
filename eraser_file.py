import cv2

def eraser(canvas,x,y):
    cv2.circle(canvas,(x+10,y+5),24,(255,255,255),cv2.FILLED)
    return canvas

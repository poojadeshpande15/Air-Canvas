import cv2

def green(canvas,x,y):
   
    cv2.circle(canvas,(x+10,y+5),8,(0,255,0),cv2.FILLED)
  
    return canvas

import cv2

def blue(canvas,x,y):
    #for i in range(x,x+2):
        
    cv2.circle(canvas,(x+10,y+5),8,(255,0,0),cv2.FILLED)
    #cv2.circle(canvas,(x+15,y+10),8,(0,255,0),cv2.FILLED)
    return canvas

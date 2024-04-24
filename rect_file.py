import cv2


def draw_rect(img):
    cv2.rectangle(img,(20,5),(100,60),(0,0,0),cv2.FILLED)
    cv2.putText(img,"ERASE ALL",(30,35),cv2.FONT_HERSHEY_SIMPLEX,0.3,(255,255,255),1)
    #cv2.rectangle(canvas,(20,5),(100,60),(0,0,0),cv2.FILLED)


    cv2.rectangle(img,(130,5),(210,60),(0,0,0),cv2.FILLED)
    cv2.putText(img,"ERASER",(140,35),cv2.FONT_HERSHEY_SIMPLEX,0.3,(255,255,255),1)

    cv2.rectangle(img,(240,5),(320,60),(0,255,0),cv2.FILLED)
    cv2.putText(img,"GREEN",(250,35),cv2.FONT_HERSHEY_SIMPLEX,0.3,(0,0,0),1)

    cv2.rectangle(img,(350,5),(430,60),(0,0,255),cv2.FILLED)
    cv2.putText(img,"RED",(360,35),cv2.FONT_HERSHEY_SIMPLEX,0.3,(0,0,0),1)

    cv2.rectangle(img,(470,5),(550,60),(255,0,0),cv2.FILLED)
    cv2.putText(img,"BLUE",(480,35),cv2.FONT_HERSHEY_SIMPLEX,0.3,(0,0,0),1)

    cv2.rectangle(img,(590,5),(630,60),(0,255,255),cv2.FILLED)
    cv2.putText(img,"SAVE",(595,35),cv2.FONT_HERSHEY_SIMPLEX,0.3,(0,0,0),1)
    
    return img

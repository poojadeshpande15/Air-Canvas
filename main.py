import numpy as np
import cv2
import time

import blur_file
import hsv_file
import track_file
import mask_file
import rect_file
import contour_file
import check_rect_file
import write_python
import read_python
import clean_file
import green_file
import eraser_file
import red_file
import blue_file


paint=True
er=False
status="draw"
f=open("mode.txt","w+")
f.write("clean")
f.close()

video=cv2.VideoCapture(0)
video.set(10,1000)

#############################################################
while True:
    check,img=video.read()
    if check==True:
        break
canvas=np.ones_like(img)*255


##############################################################
def nothing(x):
    pass

##############################################################

cv2.namedWindow("Setter")
cv2.createTrackbar("LH","Setter",0,179,nothing)
cv2.createTrackbar("LS","Setter",0,255,nothing)
cv2.createTrackbar("LV","Setter",0,255,nothing)
cv2.createTrackbar("UH","Setter",179,179,nothing)
cv2.createTrackbar("US","Setter",255,255,nothing)
cv2.createTrackbar("UV","Setter",255,255,nothing)



while True:
    _,img=video.read()
    img=cv2.flip(img,1)
    
    blur_img=blur_file.blur(img)
    hsv_img=hsv_file.hsv(blur_img)
    lh,ls,lv,uh,us,uv=track_file.track()
    mask=mask_file.mask_generator(lh,ls,lv,uh,us,uv,hsv_img)
    img=rect_file.draw_rect(img)
    x,y=contour_file.contour_operation(mask,img)

    check_rect_file.check_rect(x,y)

    status=read_python.read_file()

    

    if status=="clean":
        canvas=clean_file.clean(canvas,x,y)
        #pointer(x,y)
    if status=="green":
        canvas=green_file.green(canvas,x,y)
    if status=="eraser":
        canvas=eraser_file.eraser(canvas,x,y)
    if status=="red":
        canvas=red_file.red(canvas,x,y)
    if status=="blue":
        canvas=blue_file.blue(canvas,x,y)
    if status=="save":
        cv2.imwrite("img/pic.jpg",canvas)
        time.sleep(0.4)
        write_python.write_file("clean")


    
    op=cv2.hconcat([img,canvas])

    cv2.imshow("COMBO",op)
    #cv2.imshow("MASK",mask)
    #cv2.imshow("Blur",img)
    #cv2.imshow("Canvas",canvas)
    key=cv2.waitKey(1)
    if key==ord("q"):
        break
        
        
video.release()
cv2.destroyAllWindows()


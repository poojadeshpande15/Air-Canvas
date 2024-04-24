import cv2



def contour_operatio(mask,img):

 
    contour,_=cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    x,y,w,h=0,0,0,0
    a=(0,0)
    for cnt in contour:
        area=cv2.contourArea(cnt)
        if area>170:
            peri=cv2.arcLength(cnt,True)
            approx=cv2.approxPolyDP(cnt,0.02*peri,True)
            x,y,w,h=cv2.boundingRect(approx)
            cv2.circle(img,(x+10,y+5),8,(0,255,0),5)
            #if x!=0 or y!=0:
    return x,y
def contour_operation(mask,img):
    contour,_=cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    x,y,w,h=0,0,0,0
    if len(contour)>0:
        cnt=sorted(contour,key=cv2.contourArea,reverse=True)[0]
        area=cv2.contourArea(cnt)
        #((x,y),radius)=cv2.minEnclosingCircle(cnt)
        if area>120:
            peri=cv2.arcLength(cnt,True)
            approx=cv2.approxPolyDP(cnt,0.02*peri,True)
            x,y,w,h=cv2.boundingRect(approx)
            cv2.circle(img,(int(x),int(y)),int(w/2),(0,255,255),2)

        #M=cv2.moments(cnt)

        #x=int(M['m10']/M['m00'])
        #y=int(M['m01']/M['m00'])
    
    return x,y
        

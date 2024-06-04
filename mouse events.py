import numpy as np
import cv2

def clickEvent(event,x,y,flags,param):
    #get the x,y cordinates of the selected point
    if event == cv2.EVENT_LBUTTONDOWN:
        #match the two points
        cv2.circle(img,(x,y),5,(255,0,255),-1)
        points.append((x,y))
        if len(points)>=2:
           cv2.line(img,points[-1],points[-2],(255,0,255),5)
        cv2.imshow('image',img)
        
        '''font = cv2.FONT_HERSHEY_SIMPLEX
        text = str(x)+","+str(y)
        cv2.putText(img,text,(x,y),font,1,(255,0,0),3)
        cv2.imshow('image',img)
    #to get the color code of the selected point
    if event == cv2.EVENT_RBUTTONDOWN:
        blue = img[y,x,0]
        green = img[y,x,1]
        red = img[y,x,2]
        font = cv2.FONT_HERSHEY_SIMPLEX
        text = str(blue)+","+str(green)+","+str(red)
        cv2.putText(img,text,(x,y),font,1,(255,255,0),3)
        cv2.imshow('image',img)'''

img = np.zeros((512,512,3),np.uint8)
#img = cv2.imread('123.jpg')
cv2.imshow('image',img)
points = []
cv2.setMouseCallback('image',clickEvent)
cv2.waitKey(0)
cv2.destroyAllWindows()
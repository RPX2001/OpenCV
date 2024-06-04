import cv2
import datetime
#code for write a video file 
cap = cv2.VideoCapture(0)
forcc = cv2.VideoWriter_fourcc(*'XVID')  #four byte codec
out = cv2.VideoWriter('output.mp4',forcc,20.0,(640,480))  #writing video file file name,forcc,frame rate,size 


while(cap.isOpened()):
    ret,frame = cap.read()
    # if frame available ret = true when put if avoid unneccessary file creations
    if ret == True:
        font = cv2.FONT_HERSHEY_SIMPLEX 
        datet = str(datetime.datetime.now())
        frame = cv2.putText(frame,datet,(10,50),font,2,(0,255,255),3,cv2.LINE_AA)
        out.write(frame)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xff == ord('w'):
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()
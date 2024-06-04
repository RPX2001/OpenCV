import numpy as np
import cv2

#img = cv2.imread('123.jpg',1)
#create image using numpy zeros
img = np.zeros([512,512,3],np.uint8)
#draw a line
img = cv2.line(img,(0,0),(125,123),(0,255,0),3)
#draw arrow line 
img = cv2.arrowedLine(img,(126,0),(255,152),(255,21,0),10)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
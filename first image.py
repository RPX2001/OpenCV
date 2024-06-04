import cv2
img  = cv2.imread('123.jpg',-1)
print(img)
cv2.imshow("image",img)
k = cv2.waitKey(0)
if k == 65:
    cv2.destroyAllWindows()
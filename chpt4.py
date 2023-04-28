import cv2
import numpy as np
img = np.zeros((512,512,3),np.uint8)
#img[100:300,200:400] = 255,0,0
cv2.line(img,(0,0),(img.shape[0],img.shape[1]),(0,255,0),thickness=10)
cv2.rectangle(img,(0,0),(300,350),(0,0,255),thickness = 2)#cv2.FILLED is used to fill the rectangle rather than representing the thickness
cv2.circle(img,(250,250),50,(255,255,0),10)
cv2.putText(img,"OPENCV EXAMPLE",(100,100),cv2.FONT_HERSHEY_SIMPLEX,1,(0,150,0),1)#thickness argument must be an integer....
cv2.imshow("image",img)
cv2.waitKey(0)
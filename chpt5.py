import cv2
import numpy as np
img = cv2.imread("/Users/sandeep_munagala/Documents/opencv/wrap.PNG")
pts1 = np.float32([[423,15],[349,505],[680,563],[706,50]])
#print(pts1)
pts2 = np.float32([[0,0],[0,img.shape[0]],[img.shape[1],img.shape[0]],[img.shape[1],0]])
matrix = cv2.getPerspectiveTransform(pts1,pts2)
print(matrix)
imgOutput = cv2.warpPerspective(img,matrix,(img.shape[1],img.shape[0]))
cv2.imshow("output",imgOutput)
cv2.imshow("image",img)
cv2.waitKey(0)
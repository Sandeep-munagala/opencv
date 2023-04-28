import cv2
import numpy as np
img = cv2.imread("/Users/sandeep_munagala/Documents/opencv/opencv.PNG")
imgHor = np.hstack((img,img))
imgVer = np.vstack((img,img))
cv2.imshow("hor stack",imgHor)
cv2.imshow("ver stack",imgVer)#we can only stack the same kind of images we can't stack the diff channel images....
cv2.waitKey(0)
import cv2
import numpy as np
image = cv2.imread("resources/sharp_logo.jpg",0)
kernel = np.ones((3,3),np.float32)/9
image = cv2.resize(image,[400,300])
img = cv2.filter2D(image,ddepth=-1,kernel=kernel)
box_filter = np.hstack([image,img])
gaussian = cv2.GaussianBlur(image,(3,3),0)
gaussian_filter = np.hstack([image,gaussian])
output_image = np.vstack([box_filter,gaussian_filter])
cv2.imshow("output_image",output_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
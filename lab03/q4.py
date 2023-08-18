# importing the module
import cv2
import numpy as np
image=cv2.imread("resources/med.jpg",0)
image = cv2.resize(image,[400,300])
img = cv2.Laplacian(image,ddepth=-1,ksize=3)
output_image = np.hstack([image,img])
cv2.imshow("output_image",output_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
import cv2
import numpy as np
image=cv2.imread("resources/sharp_logo.jpg",1)
image = cv2.resize(image,[600,480])
gaussian = cv2.GaussianBlur(image,(3,3),0)
img1 = cv2.subtract(image,gaussian)
output_image = cv2.add(img1,image)
output_image = np.hstack([image,output_image])
cv2.imshow("output_image",output_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
import cv2
import numpy as np
image=cv2.imread("resources/sharp_logo.jpg",0)
image = cv2.resize(image,[400,300])
output_image = cv2.Canny(image,50,150)
img = np.hstack([image,output_image])
cv2.imshow("output image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
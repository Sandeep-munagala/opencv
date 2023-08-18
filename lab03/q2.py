import cv2
import numpy as np
kernel1 = np.array([[-1,0,1]])
#print(kernel1)
kernel2 = kernel1.T
#print(kernel2)
input_image = cv2.imread("resources/sharp_logo.jpg",0)
input_image = cv2.resize(input_image,[400,300])
k = input_image.shape
print(k)
#cv2.imshow("input image",input_image)
imgk1 = cv2.filter2D(input_image,ddepth=-1,kernel=kernel1)
#cv2.imshow("img_kernel1",imgk1)
imgk2 = cv2.filter2D(input_image,ddepth=-1,kernel=kernel2)
#cv2.imshow("img_kernel1",imgk2)
#print(imgk2.shape[0])
final_img = np.uint8(np.sqrt((imgk1*imgk1)+(imgk2*imgk2)))
final_img = final_img/255
#final_img = final_img.astype(np.uint8)
final_img = ((final_img-np.amin(final_img))/(np.amax(final_img)-np.amin(final_img)))*255
img = np.hstack([imgk1,imgk2,final_img])
#cv2.imshow("final_image",final_img)
cv2.imshow("output",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
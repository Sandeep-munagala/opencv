import cv2
img = cv2.imread("/Users/sandeep_munagala/Documents/opencv/opencv.PNG")
print(img.shape)
imgResize = cv2.resize(img,(300,200))
print(imgResize.shape)

imgCropped = img[0:100,200:500]
cv2.imshow("cropped image",imgCropped)
cv2.imshow("resize",imgResize)
cv2.imshow("image",img)
cv2.waitKey(0)
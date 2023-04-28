#color detection...
import cv2
import numpy as np
def empty(a):
    pass
cv2.namedWindow("TrackBar")
cv2.resizeWindow("TrackBar",640,240)
cv2.createTrackbar("Hue Min","TrackBar",0,179,empty)
cv2.createTrackbar("Hue Max","TrackBar",179,179,empty)
cv2.createTrackbar("sat Min","TrackBar",0,255,empty)
cv2.createTrackbar("sat Max","TrackBar",255,255,empty)
cv2.createTrackbar("v Min","TrackBar",0,255,empty)
cv2.createTrackbar("v Max","TrackBar",255,255,empty)

while True:
    img = cv2.imread("/Users/sandeep_munagala/Documents/opencv/opencv.PNG")
    img = cv2.resize(img,(480,360))
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos("Hue Min","TrackBar")
    h_max = cv2.getTrackbarPos("Hue Max","TrackBar")
    s_min = cv2.getTrackbarPos("sat Min","TrackBar")
    s_max = cv2.getTrackbarPos("sat Max","TrackBar")
    v_min = cv2.getTrackbarPos("v Min","TrackBar")
    v_max = cv2.getTrackbarPos("v Max","TrackBar")
    print(h_min,h_max,s_min,s_max,v_min,v_max)
    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
    mask = cv2.inRange(imgHSV,lower,upper)
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    cv2.imshow("mask image",mask)
    cv2.imshow("HSV image",imgHSV)
    cv2.imshow("original image",img)
    cv2.waitKey(1)
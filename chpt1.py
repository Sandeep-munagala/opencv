#to play a video.....
import cv2
cap = cv2.VideoCapture("/Users/sandeep_munagala/Documents/opencv/cv_video.mp4")
while True :
    success,img = cap.read()
    cv2.imshow("video",img)
    if cv2.waitKey(2) == ord("s"):
        break

#to display a image....
    #import cv2
    #img = cv2.imread("path file of the image")
    #cv2.imshow("nmae of the image",img)
    #cv2.waitKey(0)#...if waitkey is 0 then it stays for infinte time...



#to access our camera....
#import cv2
#cap = cv2.VideoCapture(0)
#cap.set(6,1080)
#cap.set(4,480)
#cap.set(10,100)
#while True :
#    success,img = cap.read()
#    cv2.imshow("video",img)
#    if cv2.waitKey(2) == ord("s"):
#        break
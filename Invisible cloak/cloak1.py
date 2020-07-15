from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import cv2
# first we have to capture our background color
cap = cv2.VideoCapture(0) 
while(cap.isOpened()):
    test1,img1 = cap.read()
    if(test1):
        cv2.imshow('capture',img1)
        if(cv2.waitKey(5)==ord('q')):
            cv2.imwrite('cap.jpg',img1)
            break
cap.release()
cv2.destroyAllWindows()
#          captured image will be saved in current directory


#Time for magic
cap1 = cv2.VideoCapture(0)
src = cv2.imread("cap.jpg")
while(cap1.isOpened()):
    test2,img2 = cap1.read()
    if(test2):
        #converting capturing rbg/bgr to hue 
        hsv = cv2.cvtColor(img2, cv2.COLOR_BGR2HSV)
        # I got a red cloth so, using red hue range values 
        l_hue = np.array([0,100,100])
        h_hue = np.array([10, 255, 255])
        #now masking red color 
        mask = cv2.inRange(hsv,l_hue,h_hue)
        kernel_size = 10
        kernel = np.ones((kernel_size, kernel_size), np.uint8)
        opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
        closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
        #morphology is something used to get the output more clear. you will get it once you go through offical doc at opencv.
        p1 = cv2.bitwise_and(src,src,mask=mask)
        #first get the background that to be shown when cloak is placed
        mask= cv2.bitwise_not(mask)
        p2 = cv2.bitwise_and(img2,img2,mask=mask)
        #now remove red color from picture frame
        
        cv2.imshow("win",p1+p2)
        #combine and show the cloak's magic...
        if cv2.waitKey(5) == ord('q'):# press 'q' to stop .
            break

cap1.release()
cv2.destroyAllWindows()
        
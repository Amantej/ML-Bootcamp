from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import cv2
cap = cv2.VideoCapture(0) # you can use already existed, but you have to give full location. 
classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
while(True):
    test, img = cap.read()
    if(test):
        faces = classifier.detectMultiScale(img)
        for face in faces:
            x, y, w, h = face
            facerec = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),5)
        cv2.imshow("window",facerec)
    key = cv2.waitKey(1)

    if key == ord("q"):  #press 'q' to stop your cam.
        break
    

cap.release()
cv2.destroyAllWindows()
    


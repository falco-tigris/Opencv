import cv2
import numpy as np
faceCascade = cv2.CascadeClassifier("Cascades/haarcascade_frontalcatface.xml")

img = cv2.imread("Resources/Lenna_(test_image).png")
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces = faceCascade.detectMultiScale(imgGray,1.1,1)
for (x,y,w,h) in faces:
    print(faces.shape)
    cv2.rectangle(imgGray,(x,y),(x+w,y+h),(255,0,0),2)

cv2.imshow("face image",imgGray)
cv2.waitKey(0)


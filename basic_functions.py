import cv2
import numpy as np
img = cv2.imread('Resources/2019BrazilianGrandPrixSunday_2ST8108.jpeg')
#convert from rgb to grayscale,blur image
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# cv2.imshow("Gray Image",imgGray)
# cv2.waitKey(0)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)
#finding edges in images
imgCanny = cv2.Canny(img,100,100)
kernel = np.ones((5,5),np.uint8)
imgDialation = cv2.dilate(imgCanny,kernel,iterations=1)
imgEroded = cv2.erode(imgDialation,kernel,iterations=1)
cv2.imshow("Gray Image",imgGray)
cv2.imshow("Blur Image",imgBlur)
cv2.imshow("Canny Image",imgCanny)
cv2.imshow("Dialated Image",imgDialation)
cv2.imshow("Eroded Image",imgEroded)

cv2.waitKey(0)



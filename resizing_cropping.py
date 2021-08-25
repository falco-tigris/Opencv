import cv2
import numpy as np
#resize
img = cv2.imread("Resources/2019BrazilianGrandPrixSunday_2ST8108.jpeg")
print(img.shape)
imgResize = cv2.resize(img,(300,200))
cv2.imshow("Original Image",img)
cv2.imshow("Image Resize",imgResize)
#cropping
imgCropped = img[0:200,200:500]
cv2.imshow("Cropped Image",imgCropped)
cv2.waitKey(0)







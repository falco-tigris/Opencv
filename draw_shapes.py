import numpy as np
import cv2

img = np.zeros((512,512,3),np.uint8)
print(img)
# #img[:] = 255,0,0
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3)#line img,start,end,color,thickness
cv2.imshow("line",img)
cv2.rectangle(img,(10,10),(400,450),(0,0,255))
cv2.imshow("rect",img)
# cv2.circle(img,(400,50),30,(255,0,0),3)#30 radius and400,50 centre part
# cv2.putText(img," OPENCV ",(300,200),cv2.FONT_HERSHEY_COMPLEX,2,(0,150,0),3)#300,200 starting point,2 scaling,3 thickness
# cv2.imshow("image",img)

#WARP PERSPECTIVE
# img = cv2.imread("Resources/Screen Shot 2021-08-08 at 16.26.21.png")
# width,height=250,350
# pts1 = np.float32([[111,219],[287,188],[154,482],[352,440]])
# pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
# matrix = cv2.getPerspectiveTransform(pts1,pts2)
# imgOutput = cv2.warpPerspective(img,matrix,(width,height))
# cv2.imshow("Image",img)
# cv2.imshow("Output",imgOutput)

#JOINING IMAGES
# img = cv2.imread('Resources/2019BrazilianGrandPrixSunday_2ST8108.jpeg')
# imgHor = np.hstack((img,img))
# imgVer = np.vstack((img,img))
# cv2.imshow("Horizontal",imgHor)
# cv2.imshow("Vertical",imgVer)
def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver

img = cv2.imread('Resources/Screen Shot 2021-08-08 at 16.26.21.png')
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

imgStack = stackImages(0.5,([img,imgGray,img],[img,img,img]))

cv2.imshow("Stacked",imgStack)


cv2.waitKey(0)

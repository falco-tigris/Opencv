import cv2
import numpy as np

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


def getContours(img):
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print(area)
        if area>500:
            cv2.drawContours(imgContour,cnt,-1,(255,0,0),3)
            perimeter = cv2.arcLength(cnt,True)
            print(perimeter)
            approx = cv2.approxPolyDP(cnt,0.02*perimeter,True)
            print(approx)#corner points of each shape
            print(len(approx))#no.of corners
            objcor = len(approx)
            x,y,w,h = cv2.boundingRect(approx)
            if objcor==3:
                objtype = 'Triangle'
            elif objcor==4:
                aspratio = w/float(h)
                if aspratio>0.95 and aspratio < 1.05:
                    objtype='Square'

                else:
                    objtype='Rectangle'
            elif objcor>4:

                objtype='Circle'



            else:
                objtype = 'None'
            cv2.rectangle(imgContour,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.putText(imgContour,objtype,(x+(w//2)-10,y+(h//2)-10),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255),2)













img = cv2.imread('Resources/file-shapes-for-kids-1592568510.jpeg')
imgContour = img.copy()
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),1)
imgCanny = cv2.Canny(imgBlur,50,50)

getContours(imgCanny)


imgStack = stackImages(0.8,([img,imgGray,imgBlur],[img,imgCanny,imgContour]))
cv2.imshow("Stack",imgStack)

cv2.waitKey(0)
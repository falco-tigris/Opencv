import cv2
import mediapipe as mp
import time
y1=[0,0]

mpDraw = mp.solutions.drawing_utils
mpPose = mp.solutions.pose
pose = mpPose.Pose()
cascade = cv2.CascadeClassifier('Cascades/haarcascade_fullbody.xml')
cap = cv2.VideoCapture('PoseVid/8.mp4')
pTime=0
while True:
    success,img = cap.read()
    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results = pose.process(imgRGB)
    print(results.pose_landmarks)
    if results.pose_landmarks:
        mpDraw.draw_landmarks(img,results.pose_landmarks,mpPose.POSE_CONNECTIONS)
        for id,lm in enumerate(results.pose_landmarks.landmark):
            h,w,c = img.shape

            print(id,lm)

            cx,cy=int(lm.x*w),int(lm.y*h)
            try:
                y_main = int(results.pose_landmarks.landmark[0].y*h)
                x_ear = int(results.pose_landmarks.landmark[8].x*w)
                y_ear = int(results.pose_landmarks.landmark[8].y*h)
                x_rear = int(results.pose_landmarks.landmark[7].x*w)
                y_leg = int(results.pose_landmarks.landmark[32].y*h)
                width = int(abs(int(x_ear-x_rear))+5)
                height = int(abs(int(y_ear-y_leg))+5)

                y1.append(y_main)
                gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                fb = cascade.detectMultiScale(img,1.1,3)
                # for (x,y,w,h) in fb:
                #     cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

            except:
                pass
            if((y_main-y1[-2])>30):

                cv2.putText(img, "FALL DETECTED!!!", (100, 200), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255),2)
                # cv2.rectangle(img,(x_ear,y_ear),(x_ear+width,y_ear+height),(0,0,255),3)



            cv2.circle(img,(cx,cy),5,(255,0,0),cv2.FILLED)







    cTime = time.time()
    fps = 1/(cTime-pTime)

    pTime = cTime
    cv2.putText(img,str(int(fps)),(70,50),cv2.FONT_HERSHEY_COMPLEX,3,(255,0,0),3)
    cv2.imshow("Image",img)
    cv2.waitKey(1)
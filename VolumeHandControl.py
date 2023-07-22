import cv2
import time
import handTrackingModule as htm
import math
import osascript
import numpy as np

####
wCam, hCam = 840, 480
####

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
pTime = 0
minVol = 6
maxVol = 100

detector = htm.handDetector(detectionCon=0.7)

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)
    if len(lmList)!= 0:
        #print(lmList[4], lmList[8])
        x1, y1 = lmList[4][1], lmList[4][2]
        x2, y2 = lmList[8][1], lmList[8][2]
        cx, cy = (x1+x2)//2, (y1+y2)//2

        cv2.circle(img, (x1,y1), 15, (255, 0, 255), cv2.FILLED)
        cv2.circle(img, (x2, y2), 15, (255, 0, 255), cv2.FILLED)
        cv2.line(img, (x1,y1), (x2,y2), (255, 0, 255), 3)
        cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)

        length = math.hypot(x2-x1, y2-y1)
        #print(length)
        #hand range 300 to 50
        #volume range 6 to 100

        vol = np.interp(length, [50, 300], [minVol, maxVol])
        osascript.osascript("set volume output volume {}".format(vol))

        if length< 50:
            cv2.circle(img, (cx,cy), 15, (0, 255, 0), cv2.FILLED)


    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(img, f'FPS: {int(fps)}', (40, 50), cv2.FONT_HERSHEY_PLAIN, 2 , (0, 255, 0), 2)

    cv2.imshow("Image", img)
    cv2.waitKey(1)




#import osascript
#target_volume = 50
#vol = "set volume output volume " + str(50)
#osascript.osascript(vol)

# or
#target_volume = 50
#osascript.osascript("set volume output volume {}".format(target_volume))

# or
#osascript.osascript("set volume output volume 50")

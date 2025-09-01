import cv2
import numpy as np
import pyautogui
from cvzone.HandTrackingModule import HandDetector

detector = HandDetector(maxHands=1 , detectionCon=0.8)
cap = cv2.VideoCapture(0)
screen_w , screen_h = pyautogui.size()

while True:
    success , img = cap.read()
    img = cv2.flip(img , 1)
    hands , img = detector.findHands(img , flipType=False)
    
    if hands:
        hand = hands[0]
        lmList = hand["lmList"]

        if len(lmList) != 0 :
            index_tip = lmList[8][0:2]
            x = np.interp(index_tip[0] , [0,640] , [0,screen_w])
            y = np.interp(index_tip[1] , [0,480] , [0,screen_h])
            pyautogui.moveTo(x , y)

            thumb_tip = lmList[4][0:2]
            distance = ((thumb_tip[0] - index_tip[0])**2 + (thumb_tip[1] - index_tip[1])**2)**0.5
            
            if distance < 30:
                pyautogui.click()
                cv2.circle(img , index_tip , 15 , (0,255,0) , cv2.FILLED)

    cv2.imshow("Virtual Mouse" , img)
    if(cv2.waitKey(1) & 0xFF == ord('q')):
        break

cap.release()
cv2.destroyAllWindows()
import cv2
from cvzone.HandTrackingModule import HandDetector

detector = HandDetector(maxHands=1 , detectionCon=0.8)
cap=cv2.VideoCapture(0)

def recognize_gesture(fingers):
    if fingers == [1,0,0,0,0]:
        return "Thumbs up!"
    elif fingers == [0,1,1,0,0]:
        return "Peace!"
    elif fingers == [1,0,0,0,1]:
        return "Call!"
    elif fingers == [1,1,0,0,1]:
        return "Swagy!"
    elif fingers == [1,1,1,1,1]:
        return "High Five!"
    elif fingers == [0,0,1,1,1]:
        return "Okay!"
    else:
        return "Other gesture"
    
while True: 
    success , img = cap.read()
    hands , img = detector.findHands(img)
    if hands:
        hand = hands[0]
        fingers = detector.fingersUp(hand)
        gesture = recognize_gesture(fingers)
        cv2.putText(img , gesture , (101,50) , cv2.FONT_HERSHEY_SIMPLEX , 1 , (0,255,0) , 2)
    
    cv2.imshow("Gesture Recognition" , img)
    if(cv2.waitKey(1) & 0xFF == ord('q')):
        break

cap.release()
cv2.destroyAllWindows()
    
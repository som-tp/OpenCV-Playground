import cv2
from cvzone.HandTrackingModule import HandDetector

detector = HandDetector(maxHands=2 , detectionCon=0.8)

cap = cv2.VideoCapture(0)

while True:
    success , img = cap.read()
    hands , img = detector.findHands(img)
    if hands:
        hand = hands[0]
        fingers = detector.fingersUp(hand)
        total_fingers = sum(fingers)

        cv2.putText(img , f"Fingers: {total_fingers}" , (10, 50) , cv2.FONT_HERSHEY_SIMPLEX , 1 , (255,0,0) , 2)

    cv2.imshow("Finger Counter" , img)
    if(cv2.waitKey(1) & 0xFF == ord('q')):
        break
    

cap.release()
cv2.destroyAllWindows()
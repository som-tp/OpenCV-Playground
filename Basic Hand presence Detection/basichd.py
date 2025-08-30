import cv2
from cvzone.HandTrackingModule import HandDetector

detector = HandDetector(maxHands=1, detectionCon=0.7)
cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)
    
    if hands:
        cv2.putText(img, "Hand Detected", (10, 50), 
                   cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    else:
        cv2.putText(img, "No Hand", (10, 50), 
                   cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    
    cv2.imshow("Hand Detection", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
from cvzone.HandTrackingModule import HandDetector
import cv2

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)
detector = HandDetector(detectionCon=0.5, maxHands=1)

while True:
    # Get image frame
    success, img = cap.read()

    # Find the hand and its landmarks
    img = detector.findHands(img)
    # lmList, bbox = detector.findPosition(img)
    
    # Display
    cv2.imshow("Image", img)
    # Quit on 'q' press
    if cv2.waitKey(1) == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
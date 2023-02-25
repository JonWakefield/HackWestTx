import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    
    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    
    # Apply a threshold to the grayscale image:
    _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

    # Contour detection
    contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Convex hull
    hull = []
    for i in range(len(contours)):
        hull.append(cv2.convexHull(contours[i], False))


    # Draw contours and hull
    drawing = np.zeros((thresh.shape[0], thresh.shape[1], 3), np.uint8)
    for i in range(len(contours)):
        color_contours = (0, 255, 0) # green contours
        color = (255, 0, 0) # blue hull
        cv2.drawContours(drawing, contours, i, color_contours, 1, 8)
        cv2.drawContours(drawing, hull, i, color, 1, 8)


    # Defect detection
    defects = []
    for i in range(len(hull)):
        if len(hull[i]) > 3:
            defects.append(cv2.convexityDefects(contours[i], hull[i]))


    # Display the results
    cv2.imshow('Hand Recognition', drawing)
    
    # Quit on 'q' press
    if cv2.waitKey(1) == ord('q'):
        break


print(len(hull))
print(type(drawing))


cap.release()
cv2.destroyAllWindows()
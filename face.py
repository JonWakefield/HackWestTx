import cv2

# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')



if face_cascade.empty():
    raise IOError('Unable to load the face cascade classifier xml file')

# Open webcam capture
cap = cv2.VideoCapture(0)

while True:
    # Read the frame
    ret, img = cap.read()

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    # Draw rectangles around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
        # IF WE ENTER THIS PART OF THE CODE IT MEANS A FACE HAS BEEN DETECTED:
        #print("face")

    # Show the frame
    cv2.imshow('Face detection', img)

    # Stop if 'q' key is pressed
    if cv2.waitKey(1) == ord('q'):
        break

# Release the capture and close the window


cap.release()
cv2.destroyAllWindows()
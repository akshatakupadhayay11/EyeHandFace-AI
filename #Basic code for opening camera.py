#Basic code for opening camera
import cv2

# Open the camera (0 for default camera)
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()  # Capture frame-by-frame
    if not ret:
        break

    cv2.imshow('Camera', frame)  # Display the frame

    if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to exit
        break

cap.release()
cv2.destroyAllWindows()
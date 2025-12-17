import cv2

# Initialize the camera 
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

print("Camera opened! Press 'q' to quit.")

while True:
    # Read a frame
    ret, frame = cap.read()
    
    if not ret:
        print("Failed to grab frame")
        break

    # Show the frame in a window
    cv2.imshow('Camera Test', frame)

    # Quit if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
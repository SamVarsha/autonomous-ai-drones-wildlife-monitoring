from ultralytics import YOLO
import cv2

model = YOLO('yolov8n.pt')  # Replace with animal-trained model
cap = cv2.VideoCapture('sample_forest.mp4')

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    results = model(frame)
    annotated = results[0].plot()
    cv2.imshow('Detection', annotated)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

from ultralytics import YOLO
import cv2
import os
from behaviour_tracker import BehaviorTracker  # ← Import behavior tracker

# Load YOLOv8 model
model = YOLO("yolov8n.pt")  # Make sure yolov8n.pt is in the same folder

# Load video or use webcam if file not found
video_path = "data/input_video.mp4"
cap = cv2.VideoCapture(video_path)

# Prepare video writer
os.makedirs("runs/output", exist_ok=True)
out = cv2.VideoWriter("runs/output/output_video.mp4", cv2.VideoWriter_fourcc(*'mp4v'), 20.0,
                      (int(cap.get(3)), int(cap.get(4))))

# Initialize behavior tracker
tracker = BehaviorTracker()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)[0]  # Run YOLO detection

    for box in results.boxes:
        cls_id = int(box.cls[0])
        if cls_id in [15, 16]:  # 15 = cat, 16 = dog
            label = results.names[cls_id]
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            conf = float(box.conf[0])

            # Center of bounding box
            center_x = (x1 + x2) // 2
            center_y = (y1 + y2) // 2

            # Track behavior
            tracker.track(label, (center_x, center_y), frame_id=cap.get(cv2.CAP_PROP_POS_FRAMES))

            # Draw rectangle and label
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, f"{label} {conf:.2f}", (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

    out.write(frame)
    cv2.imshow("Pet Detector", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
cap.release()
out.release()
cv2.destroyAllWindows()

# Save behavior log
tracker.save_log()

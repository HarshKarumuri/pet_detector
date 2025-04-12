import time
import pandas as pd

class BehaviorTracker:
    def __init__(self):
        self.last_positions = {}
        self.behaviors = []
    
    def track(self, pet_type, box, frame_id):
        timestamp = time.strftime("%H:%M:%S")
        x, y = int(box[0]), int(box[1])
        
        # Simple distance calculation
        if pet_type in self.last_positions:
            lx, ly = self.last_positions[pet_type]
            distance = ((x - lx) ** 2 + (y - ly) ** 2) ** 0.5
        else:
            distance = 0

        # Behavior logic
        if distance > 30:
            behavior = "Active"
        elif 10 < distance <= 30:
            behavior = "Idle"
        else:
            behavior = "Sleeping"

        self.last_positions[pet_type] = (x, y)
        self.behaviors.append({"Time": timestamp, "Pet": pet_type, "Behavior": behavior})
        print(f"[{timestamp}] {pet_type}: {behavior} (moved {distance:.1f}px)")

    def save_log(self, path="runs/output/behavior_log.csv"):
        df = pd.DataFrame(self.behaviors)
        df.to_csv(path, index=False)

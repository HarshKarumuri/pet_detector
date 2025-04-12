# 🐾 Pet Detector & Behavior Tracker using YOLOv8

This project uses **YOLOv8** to detect pets (dogs and cats) in a video or webcam stream and track their behavior (active, idle, sleeping) using simple motion-based logic. It also visualizes the behavior data with beautiful charts and animations.

---

## 💡 Features
- Detects **cats 🐱** and **dogs 🐶** using YOLOv8
- Tracks pet **movement and behavior**
- Saves annotated **output video**
- Generates a **behavior log** (`.csv`)
- Creates **animated charts** to visualize activity

---

## 🛠️ Setup

1. Clone or download this project.
2. Install the required libraries:

```bash
pip install ultralytics opencv-python pandas matplotlib seaborn plotly

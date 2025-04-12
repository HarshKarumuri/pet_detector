import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.animation import FuncAnimation

# Load the behavior log CSV
df = pd.read_csv("behavior_log.csv")

# Basic info
print("Loaded", len(df), "detections.")

# Convert time/frame to actual time (optional)
df['frame_id'] = df['frame_id'].astype(int)

# Set style
sns.set(style="darkgrid")

# Animated Plot Setup
fig, ax = plt.subplots(figsize=(10, 6))
colors = {"cat": "skyblue", "dog": "salmon"}

def animate(i):
    ax.clear()
    sample = df.iloc[:i+1]
    for label in sample['label'].unique():
        pet_df = sample[sample['label'] == label]
        ax.plot(pet_df['frame_id'], pet_df['x'], label=f"{label} X", color=colors[label])
        ax.plot(pet_df['frame_id'], pet_df['y'], label=f"{label} Y", linestyle='dashed', color=colors[label])
    
    ax.set_title("🐾 Pet Movement Over Time", fontsize=16)
    ax.set_xlabel("Frame ID")
    ax.set_ylabel("Position")
    ax.legend()
    ax.grid(True)

ani = FuncAnimation(fig, animate, frames=len(df), interval=50, repeat=False)
plt.show()

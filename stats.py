import pandas as pd
import matplotlib.pyplot as plt

# Load behavior log
log_path = "runs/output/behavior_log.csv"
df = pd.read_csv(log_path)

# Optional: Print data to confirm it's loaded
print(df.head())

# 🎯 1. Pie Chart: Behavior breakdown (Sleeping, Active, Idle)
behavior_counts = df["Behavior"].value_counts()
plt.figure(figsize=(6, 6))
plt.pie(behavior_counts, labels=behavior_counts.index, autopct='%1.1f%%', colors=["#66bb6a", "#ffa726", "#ef5350"])
plt.title("Pet Behavior Breakdown")
plt.axis("equal")
plt.show()

# 🎯 2. Bar Chart: Which pet appeared most
pet_counts = df["Pet"].value_counts()
plt.figure(figsize=(6, 4))
pet_counts.plot(kind="bar", color="#42a5f5")
plt.title("Pet Presence Count")
plt.xlabel("Pet")
plt.ylabel("Frames Detected")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

csv_path = Path("uganda_mobile_money_master_3000.csv")

if not csv_path.exists():
    raise FileNotFoundError(f"Could not find {csv_path}. Run the generator first so the CSV exists.")

df = pd.read_csv(csv_path)

if "default_label" not in df.columns:
    raise KeyError("The CSV does not contain a 'default_label' column.")

counts = df["default_label"].value_counts().sort_index()
print("Default label counts:")
print(counts)

plt.figure(figsize=(6, 4))
plt.hist(df["default_label"], bins=[-0.5, 0.5, 1.5], color="steelblue", edgecolor="black")
plt.xticks([0, 1], ["No Default", "Default"])
plt.xlabel("default_label")
plt.ylabel("Count")
plt.title("Distribution of default_label")
plt.tight_layout()
plt.show()

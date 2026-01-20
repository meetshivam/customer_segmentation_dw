import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# Load training data
df = pd.read_csv("data/customer_features.csv")

# Clean data
df = df.dropna(subset=["Monetary", "TimeSpent"])
df = df[df["Monetary"] > 0]
df.loc[df["TimeSpent"] <= 0, "TimeSpent"] = 1

# Create clean copy
X_train = df.loc[:, ["Monetary", "TimeSpent"]].copy()

# Apply same weighting as training
X_train.loc[:, "Monetary"] *= 0.7
X_train.loc[:, "TimeSpent"] *= 0.3

# Scale & PCA
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_train)

pca = PCA(n_components=2)
pca.fit(X_scaled)

# Load trained model
with open("warehouse/kmeans_model.pkl", "rb") as f:
    kmeans = pickle.load(f)

# -------- USER INPUT --------
amount = float(input("Enter amount spent: "))
time = float(input("Enter time spent (in days): "))

if time <= 0:
    time = 1

# Preprocess user input
user_data = np.array([[amount * 0.7, time * 0.3]])
user_scaled = scaler.transform(user_data)
user_pca = pca.transform(user_scaled)

# Predict cluster
cluster = kmeans.predict(user_pca)[0]

segments = {
    0: "Low Value Customer",
    1: "Loyal Customer",
    2: "High Spending Customer",
    3: "At Risk Customer"
}

print("\nCustomer Segment:", segments.get(cluster, "Unknown"))

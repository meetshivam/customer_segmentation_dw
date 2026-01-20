import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import pickle
import os

# Ensure warehouse directory exists
os.makedirs("warehouse", exist_ok=True)

# Load PCA data
df = pd.read_csv("data/pca_output.csv")
X = df[["PC1", "PC2"]]

# K-Means clustering
kmeans = KMeans(n_clusters=4, random_state=42)
df["Cluster"] = kmeans.fit_predict(X)

# Save trained model
with open("warehouse/kmeans_model.pkl", "wb") as f:
    pickle.dump(kmeans, f)

# Save clustered data
df.to_csv("data/final_clusters.csv", index=False)

# Visualization
plt.scatter(df["PC1"], df["PC2"], c=df["Cluster"])
plt.title("Customer Segmentation using K-Means")
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.show()

print("Clustering completed and model saved successfully")

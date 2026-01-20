import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# Load data
df = pd.read_csv("data/customer_features.csv")

# Drop only rows where Monetary is missing or <= 0
df = df.dropna(subset=["Monetary", "TimeSpent"])
df = df[df["Monetary"] > 0]

# Replace TimeSpent = 0 with 1 day
df.loc[df["TimeSpent"] <= 0, "TimeSpent"] = 1

# SAFETY CHECK
if df.shape[0] == 0:
    raise ValueError("No valid data available after cleaning. Check preprocessing step.")

# Create clean copy
X = df.loc[:, ["Monetary", "TimeSpent"]].copy()

# Attribute weighting
X.loc[:, "Monetary"] = X["Monetary"] * 0.7
X.loc[:, "TimeSpent"] = X["TimeSpent"] * 0.3

# Standardization
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# PCA
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

# Store PCA results
df["PC1"] = X_pca[:, 0]
df["PC2"] = X_pca[:, 1]

df.to_csv("data/pca_output.csv", index=False)

print("PCA with Attribute Weighting applied successfully")
print(f"Records processed: {df.shape[0]}")

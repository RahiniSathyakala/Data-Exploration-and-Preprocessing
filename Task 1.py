# =========================================
# LEVEL 1 - TASK 1
# Data Exploration & Preprocessing
# =========================================

import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------
# 1. Load Dataset
# -------------------------------
df = pd.read_csv("Dataset.csv")

# -------------------------------
# 2. Display first rows
# -------------------------------
print("\nFirst 5 Rows:")
print(df.head())

# -------------------------------
# 3. Number of rows and columns
# -------------------------------
print("\nDataset Shape (Rows, Columns):")
print(df.shape)

# -------------------------------
# 4. Dataset Information
# -------------------------------
print("\nDataset Info:")
df.info()

# -------------------------------
# 5. Missing Values
# -------------------------------
print("\nMissing Values in Each Column:")
print(df.isnull().sum())

# -------------------------------
# 6. Handle Missing Values
# -------------------------------
df = df.dropna()

print("\nAfter Removing Missing Values:")
print(df.isnull().sum())

# -------------------------------
# 7. Data Types
# -------------------------------
print("\nData Types:")
print(df.dtypes)

# -------------------------------
# 8. Target Variable Analysis
# -------------------------------
print("\nAggregate Rating Statistics:")
print(df['Aggregate rating'].describe())

print("\nAggregate Rating Distribution:")
print(df['Aggregate rating'].value_counts())

# -------------------------------
# 9. Visualization
# -------------------------------
plt.figure(figsize=(8,5))
df['Aggregate rating'].hist()
plt.title("Distribution of Aggregate Ratings")
plt.xlabel("Rating")
plt.ylabel("Count")
plt.show()
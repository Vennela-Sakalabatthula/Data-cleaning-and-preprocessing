import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv("student-por.csv", sep=';')

print("Original Shape:", df.shape)

# -----------------------------
# 1. Check Missing Values
# -----------------------------
print("\nMissing Values:")
print(df.isnull().sum())

# Fill missing numerical values with median
for col in df.select_dtypes(include=np.number).columns:
    df[col].fillna(df[col].median(), inplace=True)

# Fill missing categorical values with mode
for col in df.select_dtypes(include='object').columns:
    df[col].fillna(df[col].mode()[0], inplace=True)

# -----------------------------
# 2. Remove Duplicates
# -----------------------------
duplicates = df.duplicated().sum()
print("\nDuplicate Rows:", duplicates)

df = df.drop_duplicates()

# -----------------------------
# 3. Normalize Numerical Features
# -----------------------------
numerical_cols = ['age', 'absences', 'G1', 'G2', 'G3']

for col in numerical_cols:
    df[col] = (df[col] - df[col].min()) / (df[col].max() - df[col].min())

# -----------------------------
# 4. Handle Outliers (IQR Method)
# -----------------------------
for col in numerical_cols:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1

    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    df = df[(df[col] >= lower_bound) & (df[col] <= upper_bound)]

# -----------------------------
# 5. Save Clean Dataset
# -----------------------------
df.to_csv("clean_student_performance.csv", index=False)

print("\nCleaned Shape:", df.shape)
print("Cleaned dataset saved as 'clean_student_performance.csv'")
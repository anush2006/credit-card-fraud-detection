import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from config import DATASETS_DIR
import os
"""Load the credit card fraud detection dataset.
"""
df = pd.read_csv(os.path.join(DATASETS_DIR, "creditcard.csv"))

"""
Find the number of rows and columns in the dataset.
Display the first 5 rows of the dataset to have a reference.
"""
print(df.shape)
print(df.head())
"""
Describe structural information about the dataset and statistical summary of numerical columns.
(std,mean,min,max,25%/q1,50%/q2,75%/q3)
"""
print(df.info())
print(df.describe())

"""Check for missing values in the dataset.
"""
print(df.isnull().sum())

"""
Find class imbalance in the target variable 'Class'.
"""
print(df['Class'].value_counts())
print(df['Class'].value_counts(normalize=True)*100)

"""
Visualize the class balance using a count plot.
"""

sns.countplot(data=df, x='Class')
plt.title("Fraud vs Non-Fraud Count")
plt.show()

"""Visualize amount vs fraud using boxplot."""
sns.boxplot(data=df, x='Class', y='Amount')
plt.title("Amount vs Transaction Type")
plt.show()


"""Correlation analysis between features and target variable."""
plt.figure(figsize=(12,6))
sns.heatmap(df.corr(), cmap='coolwarm', linewidths=0.1)
plt.title("Correlation Heatmap")
plt.show()

"""PCA visualization of the first two principal components."""


scaler = StandardScaler()
X_scaled = scaler.fit_transform(df.drop("Class", axis=1))

pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

plt.scatter(X_pca[:,0], X_pca[:,1], c=df['Class'], cmap='coolwarm', s=2)#Scatter plot for PCA components
plt.title("PCA Visualization of Fraud Separation")
plt.show()
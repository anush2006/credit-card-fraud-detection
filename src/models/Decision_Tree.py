from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
import pandas as pd
from config import DATASETS_DIR
import os
print("Loading dataset...")
df = pd.read_csv(os.path.join(DATASETS_DIR, "creditcard.csv"))
print("Dataset loaded successfully.")
"""Seperate the features and end target"""
X=df.drop("Class",axis=1)
y=df["Class"]
print("Features and target variable separated.")
""" Splitting the dataset into training and testing sets """
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y #Stratify to maintain class distribution
)
print("Dataset split into training and testing sets.")
"""Creating Decision Tree model"""
dt_model = DecisionTreeClassifier(
    class_weight="balanced", random_state=42, max_depth=None , min_samples_split=2 )
"""Training the model"""
print("Training the Decision Tree model...")
dt_model.fit(X_train, y_train)
"""Making predictions"""
y_pred = dt_model.predict(X_test)
"""Evaluating the model"""
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred, digits=4))

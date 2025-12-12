import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix
from config import DATASETS_DIR
print("Loading dataset...")
df = pd.read_csv(os.path.join(DATASETS_DIR, "creditcard.csv"))
print("Dataset loaded successfully.")
"""Seperate the features and end target"""
X=df.drop("Class",axis=1)
y=df["Class"]
print("Features and target variable separated.")
""" Splitting the dataset into training and testing sets """
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)
print("Dataset split into training and testing sets.")
scaler = StandardScaler()
""" Normalization of data """
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
"""Creating model"""
# C=[1, 5, 10]
#gamma =[0.01, 0.1, 1] test these values 
svm_model = SVC(kernel='rbf',C=5,gamma=0.02,class_weight='balanced',random_state=42)
"""Training the model"""
print("Training the SVM model...")
svm_model.fit(X_train_scaled, y_train)
"""Making predictions"""
print("Making predictions on the test set...")
y_pred = svm_model.predict(X_test_scaled)
"""Evaluating the model"""
print("Evaluating the model...")
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred,digits=4))
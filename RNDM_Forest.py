from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
import pandas as pd

print("Loading dataset...")
df = pd.read_csv('archive/creditcard.csv')
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
rf_model = RandomForestClassifier(
    n_estimators=200,max_features=None , class_weight="balanced", random_state=42 ,n_jobs=-1)
"""Training the model"""
print("Training the Random Forest model...")
rf_model.fit(X_train, y_train)
"""Making predictions"""
print("Making predictions on the test set...")
y_pred = rf_model.predict(X_test)
"""Evaluating the model"""
print("Evaluating the model...")
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))
print("\nClassification Report:")
print(classification_report(y_test, y_pred, digits=4))

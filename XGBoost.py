from xgboost import XGBClassifier
from sklearn.metrics import confusion_matrix, classification_report
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
"""Creating XGBoost model"""
xgb = XGBClassifier(
    n_estimators=300,         # number of trees
    max_depth=5,              # depth of trees
    learning_rate=0.05,        # shrinkage to prevent overfit
    subsample=0.8,            # like RF bagging
    colsample_bytree=0.8,     # feature sampling
    scale_pos_weight=len(y_train) / sum(y_train),  # imbalance control
    random_state=42,
    n_jobs=-1, # utilize all CPU cores
    use_label_encoder=False, #do not use earlier version encoding (not needed)
    eval_metric='logloss' #general metric for binary classification another option is 'auc' 
)

"""Training the model"""
print("Training the XGBoost model...")
xgb.fit(X_train, y_train)
"""Making predictions"""
print("Making predictions on the test set...")
y_pred = xgb.predict(X_test)
"""Evaluating the model"""
print("Evaluating the model...")
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))
print("\nClassification Report:")
print(classification_report(y_test, y_pred, digits=4))

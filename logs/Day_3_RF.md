**Day-5:**

**Agenda:**
        Try improving performance using Decision Tree & Random forest and document results.
**What is Expected?:**
        The DT was already a good fit for the data and random forest will just reduce the overfitting for the data that didn't suit DT. As the data didn't overfit in the DT the gains are expected to be quite minimal. Improvements will still occur due to generalization of tree. 
**Version 1:**

n_estimators=50

Confusion Matrix:
[[56861     3]
 [   26    72]]

Classification Report:
              precision    recall  f1-score   support

           0     0.9995    0.9999    0.9997     56864
           1     0.9600    0.7347    0.8324        98

    accuracy                         0.9995     56962
   macro avg     0.9798    0.8673    0.9161     56962
weighted avg     0.9995    0.9995    0.9995     56962


**Version 2:**

n_estimators=100

Confusion Matrix:
[[56861     3]
 [   25    73]]

Classification Report:
              precision    recall  f1-score   support

           0     0.9996    0.9999    0.9998     56864
           1     0.9605    0.7449    0.8391        98

    accuracy                         0.9995     56962
   macro avg     0.9800    0.8724    0.9194     56962
weighted avg     0.9995    0.9995    0.9995     56962

Surprising results. Improved precision. Data fits well. Best trade off so far.

**Version 3:**

n_estimators=150

Confusion Matrix:
[[56861     3]
 [   24    74]]

Classification Report:
              precision    recall  f1-score   support

           0     0.9996    0.9999    0.9998     56864
           1     0.9610    0.7551    0.8457        98

    accuracy                         0.9995     56962
   macro avg     0.9803    0.8775    0.9227     56962
weighted avg     0.9995    0.9995    0.9995     56962


Minor increase. Probably not worth it to continue.


**BEST RESULT & SUMMARY:**
    Vastly improved precision compared to both baseline and DT. Best model so far.F1 score shows good trade off. Slight dip in Recall. Perhaps it could be improved using XGBoost. 

    Precision   :0.9610
    Recall      :0.7551
    f1          :0.8457
 

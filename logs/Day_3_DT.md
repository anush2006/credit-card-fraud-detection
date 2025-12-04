**Day-5:**

**Agenda:**
        Try improving performance using Decision Tree & Random forest and document results.

**Version 1:**

max_depth=8 , min_samples_split=25

Confusion Matrix:
[[55764  1100]
 [   17    81]]

Classification Report:
              precision    recall  f1-score   support

           0     0.9997    0.9807    0.9901     56864
           1     0.0686    0.8265    0.1267        98

    accuracy                         0.9804     56962
   macro avg     0.5341    0.9036    0.5584     56962
weighted avg     0.9981    0.9804    0.9886     56962

Abysmal Precision with around the same range of recall of SVM when optimized. 

**Version 2:**

max_depth=8 , min_samples_split=10 

Confusion Matrix:
[[55776  1088]
 [   17    81]]

Classification Report:
              precision    recall  f1-score   support

           0     0.9997    0.9809    0.9902     56864
           1     0.0693    0.8265    0.1279        98

    accuracy                         0.9806     56962
   macro avg     0.5345    0.9037    0.5590     56962
weighted avg     0.9981    0.9806    0.9887     56962

Still around the same precision and same recall . min_samples_split is not the limiting factor increasing depth in the next iteration.


**Version 3:**

max_depth=10 , min_samples_split=10

Confusion Matrix:
[[56350   514]
 [   21    77]]

Classification Report:
              precision    recall  f1-score   support

           0     0.9996    0.9910    0.9953     56864
           1     0.1303    0.7857    0.2235        98

    accuracy                         0.9906     56962
   macro avg     0.5650    0.8883    0.6094     56962
weighted avg     0.9981    0.9906    0.9939     56962

Recall drops sharply but significant increase in precision. Increasing the depth to 20.  

**Version 4:**

max_depth=20 , min_samples_split=10

Confusion Matrix:
[[56705   159]
 [   24    74]]

Classification Report:
              precision    recall  f1-score   support

           0     0.9996    0.9972    0.9984     56864
           1     0.3176    0.7551    0.4471        98

    accuracy                         0.9968     56962
   macro avg     0.6586    0.8762    0.7228     56962
weighted avg     0.9984    0.9968    0.9974     56962

Best result so far indicated by significantly improved f1 score. Further increasing depth and lowering minimum samples. 

**Version 5:**

max_depth=50 , min_samples_split=5

Confusion Matrix:
[[56830    34]
 [   26    72]]

Classification Report:
              precision    recall  f1-score   support

           0     0.9995    0.9994    0.9995     56864
           1     0.6792    0.7347    0.7059        98

    accuracy                         0.9989     56962
   macro avg     0.8394    0.8670    0.8527     56962
weighted avg     0.9990    0.9989    0.9990     56962

Best results as the recall seems stable even with increased depth. Setting depth to Nonde to see if it overfits.

**Version 6:**

max_depth=50 , min_samples_split=5

Confusion Matrix:
[[56830    34]
 [   26    72]]

Classification Report:
              precision    recall  f1-score   support

           0     0.9995    0.9994    0.9995     56864
           1     0.6792    0.7347    0.7059        98

    accuracy                         0.9989     56962
   macro avg     0.8394    0.8670    0.8527     56962
weighted avg     0.9990    0.9989    0.9990     56962

No change at all. Depth is no longer the limiting factor for this data. Setting minimum samples even lower to see any changes if any at all. 

**Version 7:**

max_depth=50 , min_samples_split=2

Confusion Matrix:
[[56830    34]
 [   27    71]]

Classification Report:
              precision    recall  f1-score   support

           0     0.9995    0.9994    0.9995     56864
           1     0.6762    0.7245    0.6995        98

    accuracy                         0.9989     56962
   macro avg     0.8379    0.8619    0.8495     56962
weighted avg     0.9990    0.9989    0.9989     56962

**Absolute limit reached. Best score so far.**

**BEST RESULT & SUMMARY:**

Precision   : 0.6762
Recall      : 0.7245
f1          : 0.6995  (about ~70 so very good)

Decision Tree suits this data very well and provides a very good f1 score. This is a huge improvement over SVM . The next step is to try Random Forest Classifier.
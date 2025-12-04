**Day-5:**

**Agenda:**
        Try improving performance using Decision Tree,Random forest,now XGBoost and document results.
**What is Expected?:**
        As the RF surprisingly increased precision by large amounts it is worth it to try improving upon the model using XGBoost.Test to see whether the Recall increases as the DT still holds the best recall rates so far.
**Version 1:**
Confusion Matrix:
[[56850    14]
 [   15    83]]

Classification Report:
              precision    recall  f1-score   support

           0     0.9997    0.9998    0.9997     56864
           1     0.8557    0.8469    0.8513        98

    accuracy                         0.9995     56962
   macro avg     0.9277    0.9233    0.9255     56962
weighted avg     0.9995    0.9995    0.9995     56962

Best result. High precision. High Recall. High F1 score. Probably the best generalized tree so far.

**Version 2:**

Confusion Matrix:
[[56854    10]
 [   16    82]]

Classification Report:
              precision    recall  f1-score   support

           0     0.9997    0.9998    0.9998     56864
           1     0.8913    0.8367    0.8632        98

    accuracy                         0.9995     56962
   macro avg     0.9455    0.9183    0.9315     56962
weighted avg     0.9995    0.9995    0.9995     56962

Increase in depth from 5 to 10 decreases recall but improves precision. Not what was intented but might be better for other use cases just not for this.

**Version 3:**

Confusion Matrix:
[[56854    10]
 [   17    81]]

Classification Report:
              precision    recall  f1-score   support

           0     0.9997    0.9998    0.9998     56864
           1     0.8901    0.8265    0.8571        98

    accuracy                         0.9995     56962
   macro avg     0.9449    0.9132    0.9285     56962
weighted avg     0.9995    0.9995    0.9995     56962

Reduced learning rate but it resulted in reduced precision and recall. Should try to reduce depth and see how everything changes as the depth is still 10.

**Version 4:**

Confusion Matrix:
[[56839    25]
 [   14    84]]

Classification Report:
              precision    recall  f1-score   support

           0     0.9998    0.9996    0.9997     56864
           1     0.7706    0.8571    0.8116        98

    accuracy                         0.9993     56962
   macro avg     0.8852    0.9284    0.9056     56962
weighted avg     0.9994    0.9993    0.9993     56962

Even worse . The first set of parameters were optimized. 

**BEST RESULT & SUMMARY:**

    The XGBoost did massively boost the Recall value as expected. Most optimized model so far with good generalization achieved. RF might have overfitted slightly. 

    Precision   :0.8557        
    Recall      :0.8469
    f1          :0.8513
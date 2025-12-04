
**Credit Card Fraud Detection - Final Report**

**1. Problem Understanding**

The task involved detecting fraudulent transactions in a heavily imbalanced dataset (~0.17% fraud vs ~99.83% non fraud).
The dataset contained 30 numerical input features, including Time, Amount, and PCA-transformed V1–V28 columns along with a binary Class label.
Based on initial inspection, it was clear that traditional accuracy metrics would be misleading because predicting everything as non-fraud would yield near perfect accuracy but zero real usefulness.This implied that fraud detection required attention to recall and decision boundary behaviour rather than accuracy alone.

**2. Exploratory Data Analysis Summary**

**Class Imbalance**
Fraud cases were extremely rare validating the need for specialized handling.

**Transaction Amount Behaviour**
Fraud transactions tended to occur at lower amounts, while legitimate transactions had higher outliers.

**Feature Relationships**
Correlation heatmaps showed weak and (mostly inverse) relationships with the target indicating next to no linear relationship indicators.

**PCA Scatter Plot**
There was no clear cluster separation between fraud and non-fraud cases. This supported the idea that simple linear methods would likely fail and that non-linear learning approaches, particularly ensemble methods, would be more effective.

**3. Baseline Model — Support Vector Machine**
The SVM with RBF kernel was selected as the baseline classifier after ruling out logistic regression, Naive Bayes, and KNN for conceptual reasons based on EDA results.

(C controlled misclassification penalties and gamma adjusted boundary smoothness.)
Performance was acceptable as a starting point but weak overall:

* Precision: ~0.22
* Recall: ~0.82
* F1: ~0.34

This confirmed that the dataset was non-linear and required more powerful structure-learning models.

**4. Decision Tree Results**

Decision Trees performed significantly better than SVM, capturing conditional rules and non-linear patterns.
Through tuning depth and split constraints, the best range achieved:

* Precision: ~0.70
* Recall: ~0.73–0.75
* F1: ~0.70

Decision Trees showed good potential but fluctuated based on hyperparameters, which suggested instability.

**5. Random Forest Results**

The expectation was that RF would improve slightly over Decision Trees by reducing overfitting.

However, RF far exceeded expectations:

* Precision increased sharply to ~0.96
* Recall stabilized at ~0.75
* F1 increased considerably (~0.846)

Random Forest produced extremely confident predictions, indicating strong variance reduction.
However, the drop in recall suggested that RF was slightly biased toward the majority class, possibly over-confident in its splits.

**6. XGBoost Results**

Based on the imbalance and model behaviour, XGBoost was expected to correct RF’s weakness by focusing sequentially on mistakes.

This turned out to be correct. The best model run achieved:

* Precision: ~0.86
* Recall: ~0.85
* F1: ~0.85

XGBoost significantly improved recall without sacrificing precision too heavily.
This confirmed that sequential boosting was more effective for this dataset than bagging alone.

**7. Final Model Comparison**

Summary ranking:

**Recall**

1. XGBoost
2. Decision Tree
3. Random Forest
4. SVM

**Precision**

1. Random Forest
2. XGBoost
3. Decision Tree
4. SVM

**Overall Balance (F1)**

1. XGBoost
2. Random Forest
3. Decision Tree
4. SVM

XGBoost demonstrated the best generalization and most practical behaviour for fraud detection.

**8. Technical Learnings**

* SVM struggled due to non-linear separability and imbalance.
* Decision Trees captured key relationships but could overfit without careful tuning.
* Random Forest reduced overfitting via bagging but leaned toward high precision at the expense of recall.
* XGBoost generalized best by fixing the mistakes of previous trees and applying regularization and imbalance control.

**9. Final Conclusion**

The best performing model was XGBoost, which provided the strongest precision–recall trade-off.
It generalized well and handled class imbalance effectively through its boosting approach.

* Precision: 0.8557
* Recall: 0.8469
* F1 Score: 0.8513
* Accuracy: 0.9995


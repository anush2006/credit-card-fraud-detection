Day-3 :

Finished GitHub repository setup.

Pushed Initial Commit

Loaded Kaggle dataset for credit card fraud : https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud

Completed Agenda: Data Analysis

Basic Information:

* 284,807 transactions
* 30 input features including:
*       	Time: Seconds elapsed since the first transaction
*       	Amount: Transaction value
*       	V1–V28: Principal component transformed features (anonymized)
*       	Target variable (Class):
*   		0 → Legitimate transaction
*   		1 → Fraudulent transaction
* All feature values are numerical.



Class distribution:


Class 0: 99.83 ~ percent

Class 1: 00.17 ~ percent

Huge class imbalance


Transaction Amount Patterns:


Box-plot analysis of Amount across fraud vs non-fraud classes reveals:

* Fraudulent transactions typically occur at lower monetary values.
* Legitimate transactions include a large range and high-value outliers.


Correlation analysis:


* Heatmap shows some relation ship (inverse primarily) between the features and class. However they are pretty weak.


PCA two dimensional analysis:


* Scatter plot shows no linear relationship at all. The grouping is not very clear. Fraud cases are mixed with normal ones. Normal linear models cannot distinguish properly.
  

FINAL DECISION:


Normal Linear analysis will not work well for this data as the fraudulent transactions are not distinguishable with simple models. Data augmentation must be performed to balance classes. 





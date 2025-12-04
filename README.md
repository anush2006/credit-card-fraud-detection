# Credit Card Fraud Detection (ML Practice Project)

This repository contains my work from **28/11/25 to 31/12/25**, where I practiced and strengthened my Machine Learning skills by building a fraud detection system using the Kaggle credit card fraud dataset.

The main idea was to understand how different ML models behave on **highly imbalanced**, **non-linearly separable** data and to learn proper model tuning, evaluation, and comparison.

---

## Project Goals

- Understand the dataset and analyze the imbalance problem  
- Perform EDA (distributions, PCA, correlation patterns, etc.)  
- Build a baseline classifier  
- Experiment with multiple ML algorithms  
- Tune hyperparameters and study model behavior  
- Identify the best model for fraud detection  
- Prioritize **recall** over precision (because missing fraud is worse)

More details are available in **Project_AIM.txt**.

---

## Models Implemented

The following machine learning models were trained and evaluated:

- **SVM (RBF kernel)** — used as the baseline model  
- **Decision Tree** — tuned depth & split thresholds  
- **Random Forest** — improved precision and stability  
- **XGBoost** — highest overall performance (recall, precision, F1 score)

All confusion matrices, metrics, and observations are included inside the respective scripts and in the logs.

---

## Daily Logs

A day-by-day record of the project is maintained in the `logs/` directory.

These logs include:

- model tuning attempts  
- parameter changes  
- observations  
- notes on what worked and what didn’t  

They document the entire workflow and reasoning behind each decision.

---

## Repository Structure

```
.
├── data_analysis.py         # EDA (imbalance check, PCA, plots)
├── Decision_Tree.py         # Decision Tree classifier + tuning
├── RNDM_Forest.py           # Random Forest experiments
├── SVM.py                   # Baseline SVM classifier
├── XGBoost.py               # Best performing model (boosting)
├── Data_Visualization/      # Plots generated from EDA
├── logs/                    # Day-by-day experiment logs
├── Project_AIM.txt          # Initial plan and project stages
└── requirements.txt         # Python dependencies
```

---

## Final Result

**XGBoost** achieved the best performance overall:

- **Precision:** ~0.8557  
- **Recall:** ~0.8469  
- **F1 Score:** ~0.8513  
- **Accuracy:** ~0.9995  

Since recall is more important in fraud detection, this model was selected as the final choice.

---

## Notes

- This project is only for learning and improving my ML workflow.  
- The dataset used is from Kaggle (not included in this repo).  
- All code was written and tested manually while iterating through models.

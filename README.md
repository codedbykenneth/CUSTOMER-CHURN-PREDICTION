 Telecom Churn Prediction
 Project Description
Predicts telecom customer churn using ML models based on usage, billing, and contract data. The final XGBoost model achieved 77% recall, helping identify at-risk customers and support targeted retention strategies.

 Dataset Overview
Dataset: Telecom Churn Prediction Dataset

Type: Customer subscription data

Features: Demographics, service usage, contract, billing

Target: Churn (Yes/No)

Use Cases: Churn prediction, retention, customer segmentation

 Project Goals
Analyze customer behavior and churn patterns

Build models to predict customer churn

Select the best model based on business-friendly metrics (recall, f1-score)

Identify top churn drivers using SHAP values

 Project Workflow
1. Exploratory Data Analysis (EDA)
Explored churn rates across demographics and services

Found patterns in Contract, tenure, and MonthlyCharges

2. Data Preprocessing
Handled missing values

Encoded categorical variables

Scaled numerical features for SVM

Checked multicollinearity using VIF

3. Machine Learning Models
Model	Observations
Logistic Regression	Baseline model with fair interpretability
Random Forest	Good accuracy and feature insight via SHAP
Support Vector Machine (SVM)	Struggled with class imbalance
AdaBoost	Moderate performance
XGBoost Best performing model with high recall

 Chosen Model: XGBoost
 Performance Metrics
Accuracy: 0.73

Recall: 0.77

F1-Score: 0.61

Classification Report:


              precision    recall  f1-score   support

           0       0.89      0.71      0.79      1005  
           1       0.51      0.77      0.61       393  

    accuracy                           0.73      1398  
   macro avg       0.70      0.74      0.70  
weighted avg       0.78      0.73      0.74  
 Most Important Features (from SHAP & model)
tenure

Contract

InternetService

MonthlyCharges

TotalCharges

 Business Value
Identify customers likely to churn early

Enable targeted marketing and retention strategies

Improve customer lifetime value (CLV)

 Tech Stack
Python

Pandas, NumPy, Scikit-learn

XGBoost, SHAP

Matplotlib, Seaborn

Jupyter Notebook

Streamlit

Track churn probabilities per customer

License
This project is licensed under the MIT License

Contact
Kenneth Dcunha
 kennethdcunha2004@gmail.com

import pandas as pd
#from sklearn.ensemble import RandomForestClassifier
import xgboost
from sklearn.preprocessing import LabelEncoder
from joblib import dump

# Load the dataset
telecom_cust = pd.read_csv('Telco_Customer_Churn.csv')

# Data preprocessing
# Fill missing values in 'TotalCharges' and convert to numeric
telecom_cust['TotalCharges'] = pd.to_numeric(telecom_cust['TotalCharges'], errors='coerce')
telecom_cust['TotalCharges'].fillna(0, inplace=True)

# Convert 'Churn' to binary labels
label_encoder = LabelEncoder()
telecom_cust['Churn'] = label_encoder.fit_transform(telecom_cust['Churn'])

# Use Label Encoding for 'InternetService' and 'Contract'
telecom_cust['InternetService'] = label_encoder.fit_transform(telecom_cust['InternetService'])
telecom_cust['Contract'] = label_encoder.fit_transform(telecom_cust['Contract'])

#telecom_cust['InternetService'] = telecom_cust['InternetService'].replace({'DSL':1,'Fiber Optic':2,'No':3})

# Select features
selected_features = ['tenure', 'InternetService', 'Contract', 'MonthlyCharges', 'TotalCharges']
X = telecom_cust[selected_features]
y = telecom_cust['Churn']
# Train the Random Forest model
model = xgboost.XGBClassifier(random_state = 42,max_depth =2,scale_pos_weight = 3)
model.fit(X, y)

# Save the trained model to a file
dump(model, 'Churn_XGboost.joblib')

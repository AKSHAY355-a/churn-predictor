import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import pickle

df = pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv")

#Drop customerID and missing values
df.drop("customerID", axis=1, inplace=True)
df.dropna(inplace=True)

#encode categorical variables
Label_Encoders = {}
for col in df.select_dtypes(include='object').columns:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    Label_Encoders[col] = le

selected_features = [
    'gender', 'SeniorCitizen', 'Partner', 'Dependents', 'tenure',
    'PhoneService', 'InternetService', 'Contract',
    'PaperlessBilling', 'PaymentMethod', 'MonthlyCharges', 'TotalCharges'
]

#split data 
X = df[selected_features]
y = df["Churn"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model  
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save the model and label encoders
with open("churn_model.pkl", "wb") as f:
    pickle.dump(model, f)

with open("features.pkl", "wb") as f:
    pickle.dump(selected_features, f)

with open("encoders.pkl", "wb") as f:
    pickle.dump(Label_Encoders, f)

print("Model trained and saved successfully")
import streamlit as st
import pandas as pd
import pickle

# Load the model
with open("churn_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("features.pkl", "rb") as f:
    feature_order = pickle.load(f)


st.set_page_config(page_title="Customer Churn Prediction", layout="centered")

st.title("Customer Churn Prediction System") 
st.write("Fill the customer details below to prerdict churn:")


gender = st.selectbox("Gender", ["Female", "Male"])
SeniorCitizen = st.selectbox("Senior Citizen", ["No", "Yes"])
Partner = st.selectbox("Has Partner", ["No", "Yes"])
Dependents = st.selectbox("Has Dependents", ["No", "Yes"])
tenure = st.slider("Tenure (months)", 0, 72, 12)
PhoneService = st.selectbox("Phone Service", ["No", "Yes"])
InternetService = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
Contract = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])
PaperlessBilling = st.selectbox("Paperless Billing", ["No", "Yes"])
PaymentMethod = st.selectbox("Payment Method", ["Bank transfer (automatic)", "Credit card (automatic)", "Electronic check", "Mailed check"])
MonthlyCharges = st.number_input("Monthly Charges", min_value=0.0)
TotalCharges = st.number_input("Total Charges", min_value=0.0)


# Convert categorical variables to numerical
def encode_input():
    data = {
        "gender": 1 if gender == "Male" else 0,
        "SeniorCitizen": 1 if SeniorCitizen == "Yes" else 0,
        "Partner": 1 if Partner == "Yes" else 0,
        "Dependents": 1 if Dependents == "Yes" else 0,
        "tenure": tenure,
        "PhoneService": 1 if PhoneService == "Yes" else 0,
        "InternetService": {"DSL": 0, "Fiber optic": 1, "No": 2}[InternetService],
        "Contract": {"Month-to-month": 0, "One year": 1, "Two year": 2}[Contract],
        "PaperlessBilling": 1 if PaperlessBilling == "Yes" else 0,
        "PaymentMethod": {"Bank transfer (automatic)": 0, "Credit card (automatic)": 1, "Electronic check": 2, "Mailed check": 3}[PaymentMethod],
        "MonthlyCharges": MonthlyCharges,
        "TotalCharges": TotalCharges
    }
    return pd.DataFrame([data])

#predict churn
if st.button("Predict Churn"):
    input_df = encode_input()

    # Reorder the columns to match the model's expected input
    input_df = input_df[feature_order]

    result = model.predict(input_df)[0]
    prob = model.predict_proba(input_df)[0][1]

    if result == 1:
        st.error(f"High Risk: Customer is likely to churn ({prob*100:.2f}%)")
    else:
        st.success(f"Low Risk: Customer is likely to stay ({(1-prob)*100:.2f}%)")

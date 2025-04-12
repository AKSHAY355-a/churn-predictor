# 📊 Customer Churn Prediction System

This is a machine learning web app built with **Python** and **Streamlit** that predicts whether a telecom customer is likely to **churn** (leave the service). It uses a trained **Random Forest model** and a user-friendly interface to make real-time predictions based on customer data.

---

## 🚀 Features

- ✅ Predict customer churn using a trained ML model
- 🎨 Interactive and clean Streamlit UI
- 📈 Pie chart visual for prediction probability (Soon)
- 📁 Accepts manual input from sidebar form
- 💾 Model saved using `joblib` and reused for fast prediction

---

## 🛠️ Technologies Used

- Python
- Pandas,
- Scikit-learn (RandomForestClassifier)
- Streamlit
- pickle

---

## 📷 Screenshots

| Web App Interface |
|-------------------|
| ![UI](screenshots/ui.png)

---

## 📂 Project Structure

churn-predictor/ │ ├── app.py # Streamlit app code ├── churn_model.pkl # Trained ML model ├── data/ # (Optional) Sample dataset ├── screenshots/ # Screenshots for README └── README.md # This file


---

## ▶️ How to Run Locally

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/churn-predictor.git
cd churn-predictor


pip install -r requirements.txt
streamlit run app.py
#   c h u r n - p r e d i c t o r  
 
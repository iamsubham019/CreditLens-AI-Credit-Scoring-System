# CreditLens 💳

CreditLens is an AI-powered Credit Scoring System designed to predict whether a customer is likely to default on a loan using Machine Learning techniques.

The project analyzes financial history, loan details, employment information, and credit behavior to evaluate creditworthiness and classify loan risk in real time.

---

# 🚀 Features

- Credit Risk Prediction
- Loan Default Classification
- Machine Learning-Based Scoring
- Interactive Streamlit Web Application
- Data Visualization & Exploratory Data Analysis
- Feature Importance Analysis
- Real-Time Prediction System

---

# 🧠 Machine Learning Models Used

- Logistic Regression
- Decision Tree Classifier
- Random Forest Classifier

---

# 📊 Evaluation Metrics

The models were evaluated using:

- Accuracy
- Precision
- Recall
- F1-Score
- ROC-AUC Score
- Confusion Matrix

---

# 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Streamlit
- Joblib
- Jupyter Notebook

---

# 📁 Project Structure

```text
CreditLens
│
├── app
│   └── app.py
│
├── data
│   └── credit_risk_dataset.csv
│
├── models
│   ├── credit_model.pkl
│   └── scaler.pkl
│
├── notebooks
│   └── credit_analysis.ipynb
│
├── screenshots
│
├── requirements.txt
├── README.md
└── venv
```

---

# 📂 Dataset

The dataset contains financial and behavioral information such as:

- Age
- Income
- Employment Length
- Loan Amount
- Interest Rate
- Credit History Length
- Loan Intent
- Home Ownership
- Previous Defaults

### Target Variable

- `0` → Low Credit Risk
- `1` → High Credit Risk / Default

---

# 🔍 Exploratory Data Analysis (EDA)

Performed:
- Distribution Analysis
- Correlation Heatmaps
- Outlier Detection
- Loan Default Analysis
- Feature Relationship Visualization

---

# ⚙️ Data Preprocessing

Steps included:

- Handling Missing Values
- Removing Outliers
- Label Encoding
- Feature Scaling using StandardScaler
- Train-Test Splitting

---

# 🌐 Streamlit Web Application

The Streamlit application allows users to:

- Enter financial details
- Predict credit risk
- View loan default probability instantly

---

# ▶️ How to Run the Project

## Step 1 — Clone Repository

```bash
git clone <your_repository_link>
```

---

## Step 2 — Navigate to Project Folder

```bash
cd CreditLens
```

---

## Step 3 — Create Virtual Environment

```bash
python -m venv venv
```

---

## Step 4 — Activate Environment

### Windows

```bash
venv\Scripts\activate
```

---

## Step 5 — Install Requirements

```bash
pip install -r requirements.txt
```

---

## Step 6 — Run Streamlit Application

```bash
cd app
streamlit run app.py
```

---

# 📈 Model Performance

Random Forest achieved the best overall performance with strong:

- Accuracy
- Precision
- Recall
- F1-Score

making it highly suitable for credit risk classification tasks.

---

# 📸 Screenshots

The `screenshots/` folder contains:

- Streamlit Interface
- Prediction Results
- Correlation Heatmaps
- Feature Importance Analysis
- Model Accuracy Comparison

---

# 🔮 Future Improvements

Possible future enhancements include:

- XGBoost Integration
- SHAP Explainability
- Cloud Deployment
- User Authentication
- Loan Recommendation System
- Real-Time API Integration

---

# ⭐ Conclusion

CreditLens demonstrates a complete end-to-end Machine Learning workflow including:

- Data Cleaning
- Exploratory Data Analysis
- Feature Engineering
- Model Training
- Model Evaluation
- Interactive Deployment

The project highlights the practical application of AI and Machine Learning in financial risk assessment and intelligent credit scoring systems.
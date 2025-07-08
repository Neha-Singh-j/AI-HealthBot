# AI-HealthBot - Under HACKORBIT 2025

An intelligent, rule-based medical chatbot that predicts diseases based on user-reported symptoms and provides descriptions and precautions. Built for rapid healthcare triage and awareness using real symptom-disease mappings.

---

##  Objective

To create a **medical assistant chatbot** that:
- Interacts with users to collect their symptoms.
- Predicts the most likely disease using a trained ML model.
- Returns the **description**, **severity**, and **precautionary steps** for the predicted disease.
- All built using a clean dataset of real symptoms and diseases.

---

## 📊 Dataset Overview

This project uses **4 curated CSV files**: Data Set taken from Kaggle public datasets for training model

| File Name               | Purpose                                          |
|------------------------|--------------------------------------------------|
| `dataset.csv`           | Mapping of diseases with up to 17 symptoms       |
| `Symptom-severity.csv`  | Severity scores (weights) for each symptom       |
| `symptom_Description.csv` | Description of each disease                    |
| `symptom_precaution.csv` | 4 recommended precautions per disease           |

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit** – for building a clean, interactive UI
- **Scikit-learn** – for training a Naive Bayes model
- **Pandas** – for data handling
- **Joblib** – to serialize and reuse the model

---

##  How It Works

1. **Training (`train_model.py`)**
   - Extracts and encodes all symptoms using MultiLabelBinarizer.
   - Trains a Naive Bayes classifier.
   - Saves the trained model and encoder.

2. **Chatbot Logic (`chatbot_logic.py`)**
   - Takes user-inputted symptoms.
   - Transforms them using the trained encoder.
   - Predicts the most likely disease.
   - Fetches the description and precautions.

3. **User Interface (`app.py`)**
   - Built with Streamlit.
   - Accepts comma-separated symptoms.
   - Shows predicted disease, severity, and what to do next.

---

##  Running the Project

1. **Install dependencies**
   ```bash
   pip install -r requirements.txt


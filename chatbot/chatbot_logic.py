import pandas as pd
import joblib

# Load models
model = joblib.load('model/symptom_model.pkl')
mlb = joblib.load('model/symptom_encoder.pkl')

# Load datasets
desc_df = pd.read_csv('data/symptom_Description.csv')
precaution_df = pd.read_csv('data/symptom_precaution.csv')
severity_df = pd.read_csv('data/Symptom-severity.csv')

def predict_disease(symptoms):
    symptoms = [s.strip().lower() for s in symptoms]
    input_vector = mlb.transform([symptoms])
    predicted_disease = model.predict(input_vector)[0]

    desc_row = desc_df[desc_df['Disease'] == predicted_disease]
    precautions = precaution_df[precaution_df['Disease'] == predicted_disease]

    return {
        'Disease': predicted_disease,
        'Description': desc_row['Description'].values[0] if not desc_row.empty else 'No description available',
        'Precautions': [
            precautions.get(f'Precaution_{i}', [''])[0] 
            for i in range(1, 5) if f'Precaution_{i}' in precautions
        ]
    }

def top_symptoms(n=10):
    return severity_df.sort_values(by='weight', ascending=False)['Symptom'].head(n).tolist()

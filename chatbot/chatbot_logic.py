import pandas as pd
import pickle
import numpy as np
from sklearn.preprocessing import LabelEncoder

class HealthBot:
    def __init__(self):
        # Load datasets with error handling
        try:
            self.desc_df = pd.read_csv('data/symptom_Description.csv').set_index('Disease')
            self.prec_df = pd.read_csv('data/symptom_precaution.csv').set_index('Disease')
            self.severity_df = pd.read_csv('data/Symptom-severity.csv')
            
            # Load models
            with open('model/symptom_model.pkl', 'rb') as f:
                self.model = pickle.load(f)
            with open('model/symptom_encode.pkl', 'rb') as f:
                self.encoder = pickle.load(f)
                
        except Exception as e:
            raise RuntimeError(f"Initialization failed: {str(e)}")

    def predict(self, symptoms):
        """Predict disease with severity calculation"""
        try:
            # Encode symptoms
            encoded = np.zeros(len(self.encoder.classes_))
            for s in symptoms:
                s_clean = s.strip().lower().replace(" ", "_")
                encoded[self.encoder.transform([s_clean])[0]] = 1
            
            # Predict disease
            disease = str(self.model.predict(encoded.reshape(1, -1))[0])
            
            # Get details
            description = self.desc_df.loc[disease, 'Description']
            precautions = [
                self.prec_df.loc[disease, f'Precaution_{i}'] 
                for i in range(1,5) 
                if pd.notna(self.prec_df.loc[disease, f'Precaution_{i}'])
            ]
            
            # Calculate severity score
            severity_score = 0
            for s in symptoms:
                s_clean = s.strip().lower().replace(" ", "_")
                if s_clean in self.severity_df['Symptom'].values:
                    severity_score += self.severity_df[self.severity_df['Symptom'] == s_clean]['weight'].values[0]
            
            severity = "Serious" if severity_score > 7 else "Moderate"
            
            return {
                'disease': str,
                'description': str,
                'precautions': list,
                'severity': str  # "Serious" or "Moderate"
            }
            
        except Exception as e:
            print(f"Prediction error: {e}")
            return {
                'disease': 'Unknown',
                'description': 'Diagnosis unavailable',
                'precautions': ['Please consult a doctor'],
                'severity': 'Unknown'  # Ensure severity always exists
            }

# Initialize and expose functions
bot = HealthBot()
predict_disease = bot.predict
top_symptoms = lambda: bot.severity_df.nlargest(5, 'weight')['Symptom'].tolist()
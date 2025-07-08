#  its for taiing a model for a health bot 
import pandas as pd
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.naive_bayes import MultinomialNB
import joblib
import os

# Load dataset
df = pd.read_csv('data/dataset.csv')

# Combine symptoms
symptom_cols = [col for col in df.columns if 'Symptom' in col]
df['Symptoms'] = df[symptom_cols].values.tolist()
df['Symptoms'] = df['Symptoms'].apply(lambda x: [i.strip() for i in x if pd.notna(i)])

# Encode symptoms
mlb = MultiLabelBinarizer()
X = mlb.fit_transform(df['Symptoms'])
y = df['Disease']

# Train model
model = MultinomialNB()
model.fit(X, y)

# Save model and encoder
os.makedirs('model', exist_ok=True)
joblib.dump(model, 'model/symptom_model.pkl')
joblib.dump(mlb, 'model/symptom_encoder.pkl')

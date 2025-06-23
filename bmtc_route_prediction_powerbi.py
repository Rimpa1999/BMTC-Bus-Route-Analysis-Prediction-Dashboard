
import pandas as pd
import joblib

# Load the dataset from Power BI (auto-assigned as `dataset`)
df = dataset

# Ensure necessary columns are present
if 'route_long_name' not in df.columns:
    raise ValueError("The dataset must include a 'route_long_name' column.")

# Feature engineering
df['route_long_name'] = df['route_long_name'].fillna('')
df['route_name_length'] = df['route_long_name'].apply(len)
df['is_urban'] = df['route_long_name'].str.lower().apply(
    lambda x: 1 if any(city in x for city in ['majestic', 'market', 'shivajinagar']) else 0
)

# Load the trained model (update path as per your local setup)
model = joblib.load('C:/PowerBI_BMTC/bmtc_route_type_model.pkl')

# Select features and predict
features = df[['route_name_length', 'is_urban']]
df['Predicted_Route_Type'] = model.predict(features)

# Output the dataframe with predictions
df

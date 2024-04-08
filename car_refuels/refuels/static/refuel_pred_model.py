import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import LabelEncoder
from datetime import datetime, timedelta

# Load the dataset
data = {
    'date': ['12/04/2023', '25/04/2023', '14/05/2023', '25/05/2023', '15/06/2023', '15/07/2023', '25/07/2023', '30/07/2023', '20/08/2023', '25/09/2023', '30/09/2023', '16/11/2023', '30/11/2023', '14/12/2023', '13/01/2024', '23/02/2024'],
    'fuel_type': ['Diesel', 'Diesel', 'Diesel', 'Diesel', 'Diesel', 'Diesel', 'Diesel', 'V-Power', 'V-Power', 'Diesel', 'Diesel', 'Diesel', 'Diesel', 'Diesel', 'V-Power', 'Diesel'],
    'pence_per_litre': [159.9, 156.9, 149.9, 145.9, 141.9, 140.9, 145.9, 154.9, 161.9, 158.9, 159.9, 161.9, 154.9, 149.9, 153.9, 148.9],
    'total_cost': [74.05, 71.67, 66.0, 65.54, 67.01, 64.0, 44.0, 69.01, 36.77, 51.01, 63.0, 68.69, 72.01, 66.41, 68.38, 67.53],
    'litres_filled': [46.31, 45.68, 44.03, 44.92, 47.22, 45.42, 30.16, 44.55, 22.71, 32.1, 39.4, 42.43, 46.49, 44.3, 44.43, 45.35]
}

df = pd.DataFrame(data)

# Convert date to datetime object
df['date'] = pd.to_datetime(df['date'], format='%d/%m/%Y')

# Encode fuel_type
le = LabelEncoder()
df['fuel_type'] = le.fit_transform(df['fuel_type'])

# Feature engineering: extracting date features
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month
df['day'] = df['date'].dt.day

# Predicting next refill date
X_date = df[['year', 'month', 'day']]
y_date = df['date'] + pd.DateOffset(days=30)  # Assuming next refill after 30 days

# Predicting pence per litre
X_ppl = df[['fuel_type', 'year', 'month']]
y_ppl = df['pence_per_litre']

# Predicting litres filled
X_lf = df[['fuel_type', 'pence_per_litre', 'year', 'month']]
y_lf = df['litres_filled']

# Predicting total cost
X_tc = df[['fuel_type', 'pence_per_litre', 'litres_filled', 'year', 'month']]
y_tc = df['total_cost']

# Split data into training and testing sets
X_train_date, X_test_date, y_train_date, y_test_date = train_test_split(X_date, y_date, test_size=0.2, random_state=42)
X_train_ppl, X_test_ppl, y_train_ppl, y_test_ppl = train_test_split(X_ppl, y_ppl, test_size=0.2, random_state=42)
X_train_lf, X_test_lf, y_train_lf, y_test_lf = train_test_split(X_lf, y_lf, test_size=0.2, random_state=42)
X_train_tc, X_test_tc, y_train_tc, y_test_tc = train_test_split(X_tc, y_tc, test_size=0.2, random_state=42)

# Initialize Random Forest Regressors
rf_model_date = RandomForestRegressor(n_estimators=100, random_state=42)
rf_model_ppl = RandomForestRegressor(n_estimators=100, random_state=42)
rf_model_lf = RandomForestRegressor(n_estimators=100, random_state=42)
rf_model_tc = RandomForestRegressor(n_estimators=100, random_state=42)

# Train the models
rf_model_date.fit(X_train_date, y_train_date)
rf_model_ppl.fit(X_train_ppl, y_train_ppl)
rf_model_lf.fit(X_train_lf, y_train_lf)
rf_model_tc.fit(X_train_tc, y_train_tc)

# Predict on test data
y_pred_date = rf_model_date.predict(X_test_date)
y_pred_ppl = rf_model_ppl.predict(X_test_ppl)
y_pred_lf = rf_model_lf.predict(X_test_lf)
y_pred_tc = rf_model_tc.predict(X_test_tc)

# Example prediction for next refill session
next_date_features = {
    'year': [2024],
    'month': [3],
    'day': [5]
}

next_date_df = pd.DataFrame(next_date_features)
next_date_prediction = rf_model_date.predict(next_date_df)[0]

next_ppl_features = {
    'fuel_type': [1],  # V-Power
    'year': [2024],
    'month': [3]
}

next_ppl_df = pd.DataFrame(next_ppl_features)
next_ppl_prediction = rf_model_ppl.predict(next_ppl_df)[0]

next_lf_features = {
    'fuel_type': [1],  # V-Power
    'pence_per_litre': [next_ppl_prediction],
    'year': [2024],
    'month': [3]
}

next_lf_df = pd.DataFrame(next_lf_features)
next_lf_prediction = rf_model_lf.predict(next_lf_df)[0]

next_tc_features = {
    'fuel_type': [1],  # V-Power
    'pence_per_litre': [next_ppl_prediction],
    'litres_filled': [next_lf_prediction],
    'year': [2024],
    'month': [3]
}

next_tc_df = pd.DataFrame(next_tc_features)
next_tc_prediction = rf_model_tc.predict(next_tc_df)[0]

print("Predicted next refill date:", next_date_prediction)
print("Predicted pence per litre:", next_ppl_prediction)
print("Predicted litres filled:", next_lf_prediction)
print("Predicted total cost:", next_tc_prediction)

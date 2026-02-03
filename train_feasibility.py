import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load data
df = pd.read_csv('data/original-data.csv')

def label_feasibility(row):
    # 1. Untouchable: Top tier stars (OVR 88+ or Value > 80M)
    if row['overall'] >= 88 or row['value_eur'] > 80000000:
        return 'Untouchable'
    # 2. Competitive Battle: Young stars with high potential
    elif row['potential'] > 84 and row['age'] < 25:
        return 'Competitive Battle'
    # 3. Easy Target: Older players or very low value
    elif row['age'] > 34 or row['value_eur'] < 2000000:
        return 'Easy Target'
    else:
        return 'Standard Negotiation'

df['feasibility'] = df.apply(label_feasibility, axis=1)

# Features - No scaler needed for Random Forest!
feature_cols = ['age', 'value_eur', 'overall', 'potential']
X = df[feature_cols].dropna()
y = df.loc[X.index, 'feasibility']

# Train the "Smarter" Model
rf_model = RandomForestClassifier(n_estimators=100, max_depth=10, random_state=42)
rf_model.fit(X, y)

# Save
joblib.dump(rf_model, 'models/feasibility_model.pkl')

import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
import joblib

# Load the augmented data
df = pd.read_csv('data/augmented-data.csv')

# Select the features (Physical Stats + The New Augmented Feature)
feature_cols = [
    'age', 'height_cm', 'weight_kg', 'pace', 'shooting', 
    'passing', 'dribbling', 'defending', 'physic', 'instagram_followers_m'
]
target_col = 'value_eur'

# Remove rows with missing values to ensure the model trains correctly
df_model = df[feature_cols + [target_col]].dropna()

X = df_model[feature_cols]
y = df_model[target_col]

# Split into training and testing sets (80% for training, 20% for testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the Random Forest Regressor
model_augmented = RandomForestRegressor(n_estimators=100, random_state=42)
model_augmented.fit(X_train, y_train)

# Check the Accuracy
y_pred = model_augmented.predict(X_test)
score = r2_score(y_test, y_pred)

print(f"--- Model Training Complete ---")
print(f"New Augmented Model Accuracy (R2 Score): {score:.4f}")

# Save the model
joblib.dump(model_augmented, "models/player_augmented_model.pkl")
print("Model saved as 'models/player_augmented_model.pkl'")
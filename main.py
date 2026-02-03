import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import joblib

# Load the dataset
df = pd.read_csv('data/original-data.csv')


# Display the first 5 rows
print(df.head())

# Get all column names
print(df.columns)

# Check info about data types and missing values
print(df.info())

# Quick summary statistics for numerical columns
print(df.describe())

# Missing values count
print(f"Missing values count\n{df.isnull().sum()}")
numerical_cols = ['age', 'height_cm', 'weight_kg', 'overall', 'potential']

# Function to detect outliers using IQR
def detect_outliers(df, column):
    q1 = df[column].quantile(0.25)
    q3 = df[column].quantile(0.75)
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    outliers = df[(df[column] < lower_bound) | (df[column] > upper_bound)]
    return outliers

for col in numerical_cols:
    outliers = detect_outliers(df, col)
    print(f"Column: {col} | Number of outliers: {len(outliers)}")
    print(outliers[['short_name', col]])
    print("-" * 50)

plt.figure(figsize=(15, 8))
df[numerical_cols].boxplot()
plt.title('Box Plots of Key Player Stats')
plt.show()

# As there are no missing values in the dataset
# We dont need to impute the dataset with mean, median or mode

# Encoding the data

# Nationality
new_position_col = pd.get_dummies(df['nationality'], prefix= 'nationality')
df = pd.concat([df, new_position_col], axis=1)

# Preferred foot
new_foot_col = pd.get_dummies(df['preferred_foot'], prefix='preferred_foot')
df = pd.concat([df, new_foot_col], axis=1)

# club_name
new_foot_col = pd.get_dummies(df['club_name'], prefix='club_name')
df = pd.concat([df, new_foot_col], axis=1)

# Feature engineering 
# Here we are going to calculate how much is the differnce between
# the potential of a player and the overall stats of a player

df['potential_gap'] = df['potential'] - df['overall']

# Binning Age
# 0-20 Young, 20-32 Prime, 32+ Old
df['age_group'] = pd.cut(df['age'],
                         bins=[0, 20, 32, np.inf],
                         labels=['Young', 'Prime', 'Old'],
                         include_lowest=True)

print(df.head())


feature_cols = ['age', 'height_cm', 'weight_kg', 'preferred_foot', 'pace', 'shooting', 'passing', 'dribbling', 'defending', 'physic', 'power_stamina', 'power_strength']
target_cols = ['value_eur', 'overall', 'potential']
df_model = df[feature_cols + target_cols]

# Dropping the NA values
df_model = df_model.dropna()

# Save the transformed data
df_model.to_csv('data/data-transformed.csv', index=False)

# Encoding the preferred foot column to 1 and 0
foot_map = {'Right': 1, 'Left': 0}
df_model['preferred_foot'] = df_model['preferred_foot'].map(foot_map)

X = df_model[feature_cols]
y = df_model[target_cols]

X_train, X_test, y_train, y_test = train_test_split(
    X,y, 
    test_size=0.2, 
    random_state=42)

lin_reg = LinearRegression()
lin_reg.fit(X_train, y_train)
y_pred = lin_reg.predict(X_test)

r2_values = r2_score(y_test, y_pred, multioutput='raw_values')

print("R^2 for [value_eur, overall, potential]: ", r2_values)

joblib.dump(lin_reg, "models/player_value_model.pkl")
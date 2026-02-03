import pandas as pd
import numpy as np

try:
    # Updated path to look inside the data folder
    df = pd.read_csv('data/original-data.csv')
    print("Original dataset loaded successfully.")
except FileNotFoundError:
    print("Error: 'data/original-data.csv' not found.")
    exit()

np.random.seed(42)

def calculate_hype(row):
    base_fame = ((row['overall'] + row['potential']) / 2) ** 2 / 2000
    marketability = np.random.lognormal(0, 0.5)
    followers = base_fame * marketability
    
    # Specific GOAT(Greatest of all time) Logic for Messi and Ronaldo
    if "Messi" in row['short_name'] or "Ronaldo" in row['short_name']:
        # Give them a Guaranteed massive boost regardless of randomness
        followers *= np.random.uniform(8.0, 10.0) 
    
    elif row['overall'] >= 90:
        followers *= np.random.uniform(3.0, 5.0)
    elif row['overall'] >= 85:
        followers *= np.random.uniform(1.5, 2.0)
        
    return round(followers, 1)

# Apply the logic to every player
df['instagram_followers_m'] = df.apply(calculate_hype, axis=1)

# Ensure no negative values and a minimum of 0.1M for any pro player
df['instagram_followers_m'] = df['instagram_followers_m'].clip(lower=0.1)

# Save
df.to_csv('data/augmented-data.csv', index=False)

print("--- Hype Data Generation Complete ---")
print("Top 5 'Extra Hyped' Players in your new data:")
print(df.sort_values(by='instagram_followers_m', ascending=False)[['short_name', 'overall', 'instagram_followers_m']].head(5))
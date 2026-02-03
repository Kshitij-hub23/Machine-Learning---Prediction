import streamlit as st
import joblib
import numpy as np
import pandas as pd # Added for DataFrame support

st.set_page_config(layout="wide")

st.header("Player Details (Augmented Model)")
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Profile")
    age = st.slider("Age", 15, 45, 30)
    height = st.slider("Height (cm)", 150, 205, 180)
    weight = st.slider("Weight (kg)", 45, 120, 70)
    preferred_foot = st.radio("Preferred foot", ("Left", "Right"), horizontal=True)

with col2:
    st.subheader("Technicals")
    pace = st.slider("Pace", 1, 99, 50)
    shooting = st.slider("Shooting", 1, 99, 50)
    passing = st.slider("Passing", 1, 99, 50)
    dribbling = st.slider("Dribbling", 1, 99, 50)

with col3:
    st.subheader("Physicals")
    defending = st.slider("Defending", 1, 99, 50)
    physicality = st.slider("Physicality", 1, 99, 50)
    stamina = st.slider("Stamina", 1, 99, 50)
    strength = st.slider("Strength", 1, 99, 50)

st.divider()
fame = st.slider("Instagram Followers (Millions)", 0.0, 500.0, 5.0)

# Load the models
base_model = joblib.load('models/player_value_model.pkl')
aug_model = joblib.load('models/player_augmented_model.pkl')

if st.button("Predict Augmented Value", use_container_width=True):
    preferred_foot_num = 1 if preferred_foot == "Right" else 0
    
    # 1. Define Column Names (Must match training exactly)
    base_cols = [
        'age', 'height_cm', 'weight_kg', 'preferred_foot', 
        'pace', 'shooting', 'passing', 'dribbling', 
        'defending', 'physic', 'power_stamina', 'power_strength'
    ]
    
    aug_cols = [
        'age', 'height_cm', 'weight_kg', 'pace', 'shooting', 
        'passing', 'dribbling', 'defending', 'physic', 'instagram_followers_m'
    ]

    # 2. Create DataFrames instead of np.arrays
    base_input_df = pd.DataFrame([[
        age, height, weight, preferred_foot_num, 
        pace, shooting, passing, dribbling, 
        defending, physicality, stamina, strength
    ]], columns=base_cols)

    aug_input_df = pd.DataFrame([[
        age, height, weight, pace, shooting, 
        passing, dribbling, defending, physicality, fame
    ]], columns=aug_cols)
    
    # 3. Predict
    base_results = base_model.predict(base_input_df)[0]
    base_overall = np.clip(base_results[1], 1, 99) # Clipping for realism

    aug_value = aug_model.predict(aug_input_df)[0]
    # Ensure value doesn't drop below a professional floor
    if aug_value < 50000: aug_value = 50000

    st.divider()
    res1, res2 = st.columns(2)
    
    with res1:
        st.metric("Predicted Overall (Skill)", f"{int(base_overall)}/99")
        st.write("Based strictly on performance data.")
        
    with res2:
        st.metric("Augmented Value (Market)", f"€{aug_value:,.0f}")
        st.write("Includes commercial 'Instagram Followers' metric.")

    st.success(f"With {fame}M followers, the market value is estimated at €{aug_value:,.0f}. Performance skill remains {int(base_overall)}.")
# Temporary debug check
st.write("Model expects these features:", aug_model.feature_names_in_)
import streamlit as st
import joblib
import numpy as np
import pandas as pd  # Necessary for creating the feature dataframe

# Page configuration
st.set_page_config(page_title="Player Value Predictor", layout="wide")

st.title("Player Valuation Dashboard")
st.markdown("Enter a player's physical and technical attributes below to see their predicted market standing.")

# Load the model
model = joblib.load('models/player_value_model.pkl')

st.divider()

# Input Section
with st.container():
    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("Physicality")
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
        st.subheader("Attributes")
        defending = st.slider("Defending", 1, 99, 50)
        physicality = st.slider("Physicality", 1, 99, 50)
        stamina = st.slider("Stamina", 1, 99, 50)
        strength = st.slider("Strength", 1, 99, 50)

st.divider()

# Encode preferred foot
preferred_foot_num = 1 if preferred_foot == "Right" else 0

# CREATE DATAFRAME WITH FEATURE NAMES
# Ensure these names match EXACTLY what was in your training script (X.columns)
feature_names = [
    'age', 'height_cm', 'weight_kg', 'preferred_foot', 
    'pace', 'shooting', 'passing', 'dribbling', 
    'defending', 'physic', 'power_stamina', 'power_strength'
]

input_data = pd.DataFrame([[
    age, height, weight, preferred_foot_num, 
    pace, shooting, passing, dribbling, 
    defending, physicality, stamina, strength
]], columns=feature_names)

# Prediction Button
if st.button("Generate Market Analysis", use_container_width=True):
    # Use the DataFrame instead of the raw NumPy array to avoid UserWarnings
    prediction = model.predict(input_data)
    value_pred, overall_pred, potential_pred = prediction[0]

    # PROFESSIONAL FLOOR 
    if value_pred < 50000:
        value_pred = 50000
    
    # ROUNDING
    value_pred = round(value_pred, -3) 

    # CLIP RATINGS
    overall_pred = np.clip(overall_pred, 1, 99)
    potential_pred = np.clip(potential_pred, 1, 99)

    st.subheader("Analysis Results")
    
    res_col1, res_col2, res_col3 = st.columns(3)
    
    with res_col1:
        st.metric(label="Market Value (EUR)", value=f"€{value_pred:,.0f}")
    
    with res_col2:
        st.metric(label="Current Overall", value=f"{overall_pred:.1f}/99")
    
    with res_col3:
        st.metric(label="Potential", value=f"{potential_pred:.1f}/99")
    
    st.info("Note: Market values include a €50k professional baseline for realism.")
    st.info("Note: These values are estimated based on a Linear Regression model trained on FIFA 21 data.")
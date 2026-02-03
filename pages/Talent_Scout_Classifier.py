import streamlit as st
import joblib
import numpy as np

st.set_page_config(layout="wide")

st.title("Talent Scout Classifier")
st.write("This page classifies players into squad roles using a Random Forest model.")

# Load the classifier
# Updated path to point to the models/ folder
clf = joblib.load('models/player_tier_model.pkl')

st.divider()

# Input Section (Exact same as your Predictor Page)
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Profile")
    age = st.slider("Age", 15, 45, 30)
    height = st.slider("Height (cm)", 150, 205, 180)
    weight = st.slider("Weight (kg)", 45, 120, 70)

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

if st.button("Classify Player Role", use_container_width=True):
    # Input array (11 features matching the trainer above)
    input_features = np.array([[
        age, height, weight, pace, shooting, 
        passing, dribbling, defending, physicality, 
        stamina, strength
    ]])
    
    prediction = clf.predict(input_features)[0]
    
    # Simple color coding for the text
    colors = {
        "World Class": "blue",
        "First Team": "green",
        "Rotation/Prospect": "orange",
        "Squad Filler": "red"
    }
    
    st.subheader("Scouting Report")
    st.markdown(f"### Recommended Role: :{colors[prediction]}[{prediction}]")
    st.info(f"Based on the attributes provided, this player fits into the **{prediction}** category.")
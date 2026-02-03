import streamlit as st
import joblib
import numpy as np

st.set_page_config(page_title="Transfer Feasibility Scout", layout="wide")
st.title("Transfer Feasibility Scout")

# Load the new Random Forest model
model = joblib.load('models/feasibility_model.pkl')

col1, col2 = st.columns(2)
with col1:
    val_m = st.number_input("Current Valuation (Millions EUR)", min_value=0.0, value=15.0)
    val = val_m * 1_000_000
    age = st.slider("Age", 15, 45, 24)

with col2:
    ovr = st.slider("Current Overall", 1, 99, 75)
    pot = st.slider("Potential Rating", 1, 99, 80)

if st.button("Analyze Transfer Difficulty", use_container_width=True):
    # Predict directly without scaling
    features = np.array([[age, val, ovr, pot]])
    prediction = model.predict(features)[0]
    
    st.subheader(f"Verdict: {prediction}")
    
    # UI explanation of the feasibility categories
    if prediction == 'Untouchable':
        st.write("This player is considered a core asset for their current club with a valuation that exceeds standard market limits. Negotiations would require a record-breaking offer or a high release clause activation.")
    elif prediction == 'Competitive Battle':
        st.write("This player is a high-interest target, typically due to young age and significant growth potential. Expect multiple clubs to be in contact with the agent, leading to a high-pressure negotiation environment.")
    elif prediction == 'Easy Target':
        st.write("This player is highly accessible in the current market. This status is usually due to their advanced career stage or a valuation that aligns with lower-tier budget thresholds.")
    else:
        st.write("This player represents a standard market transaction. Negotiation difficulty will be average, with the outcome depending primarily on standard contract terms and squad role promises.")
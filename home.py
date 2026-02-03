import streamlit as st

# Setup the tab name and layout
st.set_page_config(page_title="Player Analytics Pro", page_icon="⚽", layout="wide")

# Title Section
st.title("⚽ Football Player Analyser")
st.markdown("""
    Welcome to my Assistance systems project. This tool is built to show how **Machine Learning** can actually 
    help teams figure out what a player is actually worth and how good they can become. 
    Instead of just guessing, we're using data on thousands of players to find real patterns.
""")

st.divider()

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Data-Driven Stats")
    st.write("""
        We analyze 12 key features—including pace, shooting, and physicality—to 
        calculate a player's current skill level and future Potential.
    """)

with col2:
    st.subheader("Valuation")
    st.write("""
        The model predicts a player's market value in Euros.
    """)

with col3:
    st.subheader("Fame Factor")
    st.write("""
        On the **Augmented Data** page, I've added a social media fame variable to show how 
        things like 'Instagram Followers' can drive up market prices without changing a player's actual skill.
    """)

st.divider()

# Quick Navigation Guide
st.header("How to use the tool")
st.write("""
    * **Chatbot:** Ask the AI questions about specific players or general stats.
    * **Standard Predictor:** Use the 12 technical sliders to see a player's predicted rating and price.
    * **Augmented Predictor:** See how 'Instagram Fame' affects the valuation model specifically.
""")

# Database info
st.info("Built using the FIFA 21 Dataset.")
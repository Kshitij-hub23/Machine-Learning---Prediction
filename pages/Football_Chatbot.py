import streamlit as st
import pandas as pd
import difflib
import speech_recognition as sr
from gtts import gTTS
import io

st.set_page_config(page_title="FootyBot", page_icon="⚽", layout="centered")

# Styling to handle chat input and layout
st.markdown("""
    <style>
    .block-container { padding-bottom: 150px; }
    .stChatInputContainer { background-color: transparent; }
    </style>
    """, unsafe_allow_html=True)

def generate_speech(text: str, auto_play=False):
    """Generates and plays voice output using gTTS."""
    if text:
        try:
            tts = gTTS(text=text, lang='en')
            audio_buffer = io.BytesIO()
            tts.write_to_fp(audio_buffer)
            audio_buffer.seek(0)
            st.audio(audio_buffer, format="audio/mp3", autoplay=auto_play)
        except Exception:
            pass

def listen_command():
    """Captures voice input from the microphone."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.toast("Record 🎤 Listening... Speak now!")
        r.adjust_for_ambient_noise(source, duration=0.5)
        try:
            audio = r.listen(source, timeout=4, phrase_time_limit=7)
            text = r.recognize_google(audio)
            return text
        except:
            st.error("Couldn't hear you clearly.")
            return None

@st.cache_data
def load_data():
    """Loads the original dataset as required by the project specs."""
    return pd.read_csv("data/original-data.csv")

df = load_data()

# Initialize session state for conversation history (10+ conversations requirement)
if "messages" not in st.session_state:
    st.session_state.messages = []

with st.sidebar:
    st.title("Settings")
    st.write("Use Voice Search if you don't want to type.")
    if st.button("🎙️ Start Voice Input", use_container_width=True):
        spoken = listen_command()
        if spoken:
            st.session_state.voice_input = spoken
            st.rerun()
    st.divider()
    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.rerun()

st.title("⚽ FootyBot AI")
st.caption("Your FIFA 21 Stats Assistant")

# Display chat history
for i, msg in enumerate(st.session_state.messages):
    with st.chat_message(msg["role"]):
        st.write(msg["content"])
        if msg["role"] == "assistant":
            if st.button("🔊", key=f"spk_{i}"):
                generate_speech(msg["content"], auto_play=True)

# Handle Chat Input (Text or Voice)
prompt = st.chat_input("Ask me about a player, club, or top stats...")

if "voice_input" in st.session_state:
    prompt = st.session_state.voice_input
    del st.session_state.voice_input

if prompt:
    # Add User Message to history
    st.session_state.messages.append({"role": "user", "content": prompt})

    text_query = prompt.lower().strip()
    reply = ""

    # Greeting
    if any(text_query.startswith(g) for g in ["hi", "hello", "hey"]):
        reply = "Hey! I'm FootyBot ⚽. I can find player stats, identify top players, or analyze club averages!"

    # Dataset Stats (Numerical Requirement)
    elif "how many" in text_query:
        reply = f"I have data on {len(df):,} players from the FIFA 21 database."

    # Top Players by Attribute (Statistical Analysis Requirement)
    elif "best" in text_query or "top" in text_query:
        attribute = "overall"
        if "pace" in text_query: attribute = "pace"
        elif "shoot" in text_query: attribute = "shooting"

        top_players = df.nlargest(5, attribute)[["short_name", attribute]]
        reply = f"Here are the top 5 players for **{attribute}**:\n\n"
        for _, row in top_players.iterrows():
            reply += f"• {row['short_name']}: {row[attribute]}\n"

    # High Growth Potential (Golden Prospects)
    elif "potential" in text_query or "growth" in text_query:
        df['growth'] = df['potential'] - df['overall']
        prospects = df[df['age'] < 23].nlargest(3, 'growth')
        reply = "High-growth prospects (under 23) found in the data:\n\n"
        for _, row in prospects.iterrows():
            reply += f"• **{row['short_name']}**: {row['overall']} -> {row['potential']} (+{row['growth']})\n"

    # Club / Team Search (Average Rating Analysis)
    elif "club" in text_query or "team" in text_query:
        words = text_query.split()
        club_name = words[-1]
        club_df = df[df['club_name'].str.lower().str.contains(club_name, na=False)]

        if not club_df.empty:
            avg_ovr = club_df['overall'].mean()
            reply = f"In **{club_name.title()}**, I found {len(club_df)} players. Their average squad rating is {avg_ovr:.1f}."
        else:
            reply = f"I couldn't find any data for the club '{club_name}'."

    # Random Player
    elif "random" in text_query:
        row = df.sample(1).iloc[0]
        reply = f"Check out **{row['short_name']}**! They have an overall rating of {row['overall']}."

    # Specific Player Search
    else:
        words_to_remove = ["stat", "overall", "pace", "shoot", "pass", "dribbl", "who is", "who's", "?"]
        cleaned = text_query
        for word in words_to_remove:
            cleaned = cleaned.replace(word, "")

        matches = difflib.get_close_matches(cleaned.strip(), df["short_name"].str.lower().tolist(), n=1, cutoff=0.5)

        if matches:
            match = matches[0]
            p = df[df["short_name"].str.lower() == match].iloc[0]
            reply = (f"**{p['short_name']}** stats:\n\n"
                     f"⚽ Overall: {p['overall']}\n"
                     f"⚡ Pace: {p['pace']} | 🎯 Shooting: {p['shooting']}\n"
                     f"🪄 Passing: {p['passing']} | 🧊 Dribbling: {p['dribbling']}")
        else:
            reply = "I couldn't find that player or intent. Try asking for 'best pace' or 'Lionel Messi'."

    st.session_state.messages.append({"role": "assistant", "content": reply})
    st.rerun()
import streamlit as st
import google.generativeai as genai
import json

# --- CONFIGURATION ---
API_KEY = "AIzaSyDs78N17p1UrPSUBl-Z_f5qt_Uo2cAygYo"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-2.5-flash')

# --- FAKE DATABASE (The "Context") ---
users_db = [
    {"name": "Aarav", "age": 22, "bio": "Tech bro by day, gamer by night. Loves valorant and coding.", "vibe": "Introverted & Logical"},
    {"name": "Priya", "age": 21, "bio": "Art student. Obsessed with astrology, indie music and thrifting.", "vibe": "Creative & Spiritual"},
    {"name": "Rohan", "age": 23, "bio": "Gym rat. Protein shakes and startups. Hustle culture.", "vibe": "High Energy & Ambitious"},
    {"name": "Sanya", "age": 22, "bio": "Backpacking across India. Photographer. Loves spicy food.", "vibe": "Adventurous & Free-spirited"}
]

st.set_page_config(page_title="💘 Cupid's Agent", page_icon="💘")

st.title("💘 Cupid's Autonomous Agent")
st.subheader("Tell me what you are looking for, and I'll find your match.")

user_query = st.text_input("Describe your ideal partner (e.g., 'Someone to go hiking with'):")

# The "Agentic" Logic
# We feed the DB into the prompt (RAG-lite)
agent_prompt = f"""
You are an AI Matchmaking Agent. You have access to the following user database:
{json.dumps(users_db)}

Your User is asking for: "{user_query}"

Task:
1. Analyze the User's request.
2. Compare it against the profiles in the database.
3. Select the ONE best match based on shared interests and vibe.
4. Explain WHY you chose them using psychological reasoning.

Output format:
**Best Match:** [Name]
**Match Score:** [0-100]%
**Reasoning:** [Your explanation]
"""

if st.button("Find Match"):
    if user_query:
        with st.spinner("Agent is analyzing compatibility vectors..."):
            response = model.generate_content(agent_prompt)
            st.success("Match Found!")
            st.markdown(response.text)
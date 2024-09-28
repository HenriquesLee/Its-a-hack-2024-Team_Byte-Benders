import streamlit as st

st.title("📖 README")
# Set the background image using HTML and CSS
background_image = """
<style>
[data-testid="stSidebarContent"] {
    background-image: linear-gradient(to bottom right, #290e47, #341c5c);
}
[data-testid="stAppViewContainer"] > .main {
    background-image: url("https://media1.tenor.com/m/HkBmWN8onyUAAAAC/bg.gif");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
}
[data-testid="stHeader"] {
    background-color: rgba(0, 0, 0, 0);
}
</style>
"""
st.markdown(background_image, unsafe_allow_html=True)

st.write("""
*NeuroSync* is designed to help individuals improve focus, productivity, and effectively manage their goals. This tool is ideal for students preparing for exams such as GATE, CAT, and JEE Advanced, as well as professionals looking to increase work efficiency.

### Key Features:
- *AI Chatbot for Assistance*: Ask the AI questions related to productivity, study plans, or general queries.
- *Goal Tracking System*: Track daily, weekly, and monthly goals to maintain consistency.
- *Daily Streaks*: Challenge yourself to complete daily goals and maintain long streaks.
- *Motivational Messages*: Based on how you're feeling, AI will generate personalized motivation.
- *Customizable Study Plan*: Enter your schedule and goals, and the AI will create a personalized focus or study plan for you.
- *Productivity Analytics*: Track and visualize your progress over time to understand where improvements are needed.

---

### Installation & Setup:
To get started with NeuroSync, follow these steps:

1. *Clone the repository*:
    bash
    git clone https://github.com/HenriquesLee/Its-a-hack-2024-Team_Byte-Benders.git
    

2. *Install the dependencies*:
    bash
    pip install -r requirements.txt
    

3. *Run the app*:
    bash
    streamlit run app.py
    

---

### Tech Stack:
- *Frontend*: Streamlit for building a fast and interactive web interface.
- *Backend*: Python and Google Gemini API for AI-driven responses and embeddings.
- *Database*: SQLite for tracking goals and user progress.
- *AI Integrations*: Google Gemini for natural language processing, study plan generation, and motivational content.

---

We hope NeuroSync helps you achieve your goals efficiently. Happy focusing!
""")
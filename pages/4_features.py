import streamlit as st

st.title("✨ Features of NeuroSync")

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
NeuroSync is packed with a wide range of features aimed at enhancing focus and productivity. Here are the detailed functionalities:

---

### 1. **AI-Powered Chatbot** 🤖
NeuroSync provides an AI assistant, powered by the **Google Gemini API**, that can answer any productivity-related questions. This includes generating study plans, suggesting tips for managing your time, and even offering advice on how to stay motivated.

---

### 2. **Goal Tracking** 🎯
NeuroSync allows users to set **daily, weekly, monthly**, and even **long-term goals**. The AI not only helps track progress but also suggests changes or improvements if certain goals are falling behind.

---

### 3. **Daily Streaks** 🔥
Stay motivated by building streaks for completing your tasks. NeuroSync records how long you've consistently met your daily goals and motivates you to maintain longer streaks.

---

### 4. **Motivational Messages** 💬
Feeling low or demotivated? NeuroSync understands your feelings through simple input and responds with personalized motivational messages to keep you going.

---

### 5. **Custom Focus/Study Plan** 📅
One of the core features of NeuroSync is the **AI-generated focus/study plan**. Enter your preparation level, your exam date, and your daily schedule. The AI will generate a complete plan that breaks down your time into manageable tasks.

---


### 6. **Timeline for Exam Preparation** 🕒
For students preparing for competitive exams like GATE, CAT, or JEE, NeuroSync provides a countdown to the exam date, along with a detailed breakdown of what should be achieved each day leading up to the exam.
""")

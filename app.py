import streamlit as st
import sqlite3
from ai_module import generate_focus_plan, ai_chat
from streaks_module import get_streaks, update_streaks
from user_goals import set_goals, view_goals
from motivation_module import get_motivational_message
from focus_mode import start_focus_session
from study_planner import study_planner
from task_manager import manage_tasks
from analytics import show_analytics

# Initialize SQLite3 connection
conn = sqlite3.connect('neurosync.db')
cursor = conn.cursor()

# Create necessary tables
cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    purpose TEXT,
                    focus_plan TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                  )''')

cursor.execute('''CREATE TABLE IF NOT EXISTS streaks (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER,
                    streak INTEGER,
                    last_update DATE,
                    FOREIGN KEY(user_id) REFERENCES users(id)
                  )''')

cursor.execute('''CREATE TABLE IF NOT EXISTS goals (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER,
                    goal_type TEXT,
                    goal_description TEXT,
                    due_date DATE,
                    FOREIGN KEY(user_id) REFERENCES users(id)
                  )''')

conn.commit()

# App UI
st.title("NeuroSync: AI-Driven Focus and Productivity Maximizer")

# User Input
user_name = st.text_input("Enter your name")
purpose = st.selectbox("Choose your purpose", ("General Productivity", "Entrance Exam: GATE", "Entrance Exam: CAT", "Entrance Exam: JEE Advanced"))

if user_name and purpose:
    # Add user to DB if not already exists
    user_exists = cursor.execute("SELECT id FROM users WHERE name=?", (user_name,)).fetchone()
    if not user_exists:
        cursor.execute("INSERT INTO users (name, purpose) VALUES (?, ?)", (user_name, purpose))
        conn.commit()

    # Navigation Dropdown
    page_selection = st.sidebar.selectbox("Select an option", 
                                          ["Generate AI Focus Plan", 
                                           "Chat with AI for Doubts", 
                                           "Daily Streaks", 
                                           "Set and View Goals", 
                                           "Get Motivation",
                                           "Start Focus Mode",
                                           "Study Planner",
                                           "Manage Tasks"])
    
    if page_selection == "Generate AI Focus Plan":
        st.subheader("Generate AI Focus Plan")
        if st.button("Generate Focus Plan"):
            focus_plan = generate_focus_plan(purpose)
            st.write(f"AI Focus Plan: {focus_plan}")
    
    elif page_selection == "Chat with AI for Doubts":
        st.subheader("Chat with AI for Doubts")
        user_question = st.text_input("Ask a question")
        if user_question:
            ai_response = ai_chat(user_question)
            st.write(f"AI Response: {ai_response}")
    
    elif page_selection == "Daily Streaks":
        st.subheader("Daily Streaks")
        streak_data = get_streaks(user_name)
        
        if streak_data:
            # Print the streak count in bold using Markdown
            st.markdown(f"**Current Streak:** {streak_data['streak']} days")
            st.markdown(f"Last Update: {streak_data['last_update']}")
        else:
            st.write("No streaks found. Start your streak today!")
        
        if st.button("Update Streak"):
            update_streaks(user_name)
            st.success("Streak updated!")
        
    elif page_selection == "Set and View Goals":
        st.subheader("Set and View Goals")
        set_goals(user_name)
        view_goals(user_name)
    
    elif page_selection == "Get Motivation":
        st.subheader("How do you feel?")
        feeling = st.selectbox("Select your current feeling", ("Motivated", "Tired", "Anxious", "Excited"))
        if st.button("Get Motivation"):
            motivational_message = get_motivational_message(feeling)
            st.write(f"Motivation: {motivational_message}")
    
    elif page_selection == "Start Focus Mode":
        start_focus_session()  # Starts focus mode
    
    elif page_selection == "Study Planner":
        study_planner()  # Starts study planner session
    
    elif page_selection == "Manage Tasks":
        manage_tasks()  # Task manager
    

else:
    st.warning("Please enter your name and select your purpose before proceeding.")

import sqlite3
import streamlit as st
import datetime

def set_goals(user_name):
    goal_type = st.selectbox("Select goal type", ("Daily", "Weekly", "Monthly", "Quarterly"))
    goal_description = st.text_input("Enter your goal description")
    due_date = st.date_input("Select due date")
    
    if st.button("Set Goal"):
        conn = sqlite3.connect('neurosync.db')
        cursor = conn.cursor()
        user_id = cursor.execute("SELECT id FROM users WHERE name=?", (user_name,)).fetchone()[0]
        cursor.execute("INSERT INTO goals (user_id, goal_type, goal_description, due_date) VALUES (?, ?, ?, ?)", (user_id, goal_type, goal_description, due_date))
        conn.commit()
        conn.close()
        st.success("Goal added successfully!")

def view_goals(user_name):
    conn = sqlite3.connect('neurosync.db')
    cursor = conn.cursor()
    cursor.execute("SELECT goal_type, goal_description, due_date FROM goals WHERE user_id = (SELECT id FROM users WHERE name=?)", (user_name,))
    goals = cursor.fetchall()
    conn.close()

    if goals:
        for goal in goals:
            st.write(f"Goal Type: {goal[0]}")
            st.write(f"Goal Description: {goal[1]}")
            st.write(f"Due Date: {goal[2]}")
            st.write("---")
    else:
        st.write("No goals found.")

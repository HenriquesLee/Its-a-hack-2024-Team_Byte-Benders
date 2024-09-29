import streamlit as st
from ai_module import prioritize_tasks  # Import the AI function

def manage_tasks():
    st.subheader("📝 Task Manager & Prioritization")
    
    task_list = st.text_area("Enter your tasks (one per line)")
    priority_button = st.button("Prioritize Tasks")
    
    if priority_button:
        tasks = task_list.split("\n")
        if tasks:
            with st.spinner('Prioritizing your task...'):# Check if there are any tasks entered
                prioritized_tasks = prioritize_tasks(tasks)  # Call the AI function
            st.write("Your prioritized tasks are:")
            st.write(prioritized_tasks)
        else:
            st.warning("Please enter at least one task to prioritize.")

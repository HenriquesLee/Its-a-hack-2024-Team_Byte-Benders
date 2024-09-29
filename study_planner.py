import streamlit as st
import json
import os
from ai_module import generate_study_plan

def study_planner():
    st.subheader("📚 Personalized Study Planner")
    
    exam_type = st.selectbox("Choose Exam", ["GATE", "CAT", "JEE Advanced", "General Purpose"])
    num_weeks = st.number_input("How many weeks until your exam?", 1, 52)
    
    generate_button = st.button("Generate Study Plan")
    
    if generate_button:
        # Call the AI function to generate the study plan
        with st.spinner('Cooking your study plan...'):
            study_plan = generate_study_plan(exam_type, num_weeks)

        # Debugging: Print the raw output
        st.write("Raw output from AI:", study_plan)

        # Check if the response is a valid JSON string
        try:
            study_plan_dict = json.loads(study_plan)  # Attempt to load the response as JSON
            st.json(study_plan_dict)

            # Ensure the 'data' directory exists
            data_directory = "data"
            if not os.path.exists(data_directory):
                os.makedirs(data_directory)

            # Write the study plan to a JSON file
            with open(f"{data_directory}/{exam_type}_study_plan.json", "w") as f:
                json.dump(study_plan_dict, f)
            st.success(f"Your {exam_type} Study Plan has been saved!")
        except json.JSONDecodeError:
            st.error("Failed to generate a valid study plan. Please try again.")
            st.write("Invalid JSON response:", study_plan)  # Print the invalid response
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

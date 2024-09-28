import google.generativeai as genai
import os

# Configure Gemini API with the correct key
genai.configure(api_key="AIzaSyD1h8zNaWMAVk5VMDkyNZL2ByCaJwOGX9Y")

# Load the model
model = genai.GenerativeModel('gemini-1.5-pro-001')

# Function to generate a personalized focus plan
def generate_focus_plan(purpose):
    try:
        # Send a request to the Gemini API to generate a focus plan
        prompt = f"Generate a personalized focus plan for {purpose}."
        response = model.generate_content(prompt)

        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

# AI chat function for general questions
def ai_chat(user_question):
    try:
        # Send the question to the Gemini API
        response = model.generate_content(user_question)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

# AI function for generating study plans
def generate_study_plan(exam_type, num_weeks):
    prompt = f"Create a personalized study plan for {exam_type} preparation over {num_weeks} weeks."
    try:
        response = model.generate_content(prompt)
        return response.text  # Return the AI-generated study plan
    except Exception as e:
        return f"Error: {str(e)}"


# AI function for prioritizing tasks
def prioritize_tasks(tasks):
    prompt = "Prioritize the following tasks based on their urgency and importance:\n" + "\n".join(tasks)
    try:
        # Send the prompt to the Gemini API
        response = model.generate_content(prompt)
        return response.text  # Return the AI-generated prioritized tasks
    except Exception as e:
        return f"Error: {str(e)}"

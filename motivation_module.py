import google.generativeai as genai
import streamlit as st

# Configure the API key (replace with your own key)
genai.configure(api_key="YOUR_API_KEY_HERE")
model = genai.GenerativeModel('gemini-1.5-pro-001')

# Function to generate a motivational message
def get_motivational_message(feeling):
    prompt = f"I am feeling {feeling}. Please provide some motivational advice."
    try:
        response = model.generate_content(prompt)
        return response.candidates[0].content
    except Exception as e:
        return f"Error: {str(e)}"

# Streamlit UX implementation
def display_motivational_message():
    st.header("🌟 Daily Motivation")
    
    # User input for feelings using radio buttons
    feeling = st.radio("How are you feeling today?", 
                       ["Motivated", "Tired", "Anxious", "Excited", "Stressed", "Happy", "Overwhelmed"])

    if st.button("Get Motivation"):
        # Fetch the motivational message
        message = get_motivational_message(feeling)

        # Display the message in an overlay-like dialogue box
        if message:
            st.markdown(f"""
            <div style="background-color: rgba(30, 144, 255, 0.9); padding: 20px; border-radius: 10px; color: white; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);">
                <h3>🧘‍♂️ Your Motivational Thought of the Day:</h3>
                <p>{message}</p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.warning("Could not retrieve a motivational message. Please try again.")

# Main app function
def main():
    st.sidebar.title("💡 Motivation Hub")
    st.sidebar.info("Get your personalized motivational thought based on how you're feeling.")
    
    display_motivational_message()

if __name__ == "__main__":
    main()

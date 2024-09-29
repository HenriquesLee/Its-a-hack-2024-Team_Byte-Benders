import streamlit as st
import google.generativeai as genai

# Configure the API key (replace with your own key)
genai.configure(api_key="YOUR_API_KEY_HERE")
model = genai.GenerativeModel('gemini-1.5-pro-001')

# Function to generate a friendly response
def get_study_buddy_response(user_input):
    try:
        with st.spinner('Analyzing...'):
            prompt = f"My friend is telling me about their day: '{user_input}'. How should I respond in a supportive and friendly way? Don't write in points but respond in a paragraph as if you were directly talking to them."
            response = model.generate_content(prompt)

        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

# Streamlit UX for the Study Buddy
def display_study_buddy():
    st.header("👫 Study Buddy - Your AI Companion")

    # Ask the user how their day went
    user_day = st.text_area("How was your day?", placeholder="Tell me how your day went...")

    # If user writes about their day, generate a response
    if st.button("Submit"):
        if user_day:
            response = get_study_buddy_response(user_day)
            # Display the AI's friendly response
            st.markdown(f"""
                <div style="background-color: rgba(0, 0, 0, 0.9); padding: 20px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);">
                <h3>🗨️ Study Buddy says:</h3>
                <p>{response}</p>
                </div>
            """, unsafe_allow_html=True)
        else:
            st.warning("Please tell me how your day was!")

# Main function to run the app
def main():
    display_study_buddy()

if __name__ == "__main__":
    main()

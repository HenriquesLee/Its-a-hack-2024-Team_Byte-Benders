import google.generativeai as genai

# Configure the API key (replace with your own key)
genai.configure(api_key="YOUR_API_KEY_HERE")
model = genai.GenerativeModel('gemini-1.5-pro-001')


def get_motivational_message(feeling):
    prompt = f"I am feeling {feeling}. Please provide some motivational advice."
    try:
        # Use the generate method for chat-like responses
        response = model.generate_content(prompt)
        
        
        # Return the generated content
        return response.candidates[0].content
    except Exception as e:
        return f"Error: {str(e)}"


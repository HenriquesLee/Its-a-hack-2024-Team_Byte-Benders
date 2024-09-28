import requests
import google.generativeai as genai
import os

# Replace with your Gemini API key
GEMINI_API_KEY = "YOUR_API_KEY_HERE"

# Configure the Gemini API key
genai.configure(api_key=GEMINI_API_KEY)

def ask_llm():
    st.subheader("💬 Ask Gemini LLM")
    
    question = st.text_input("Enter your question")
    if st.button("Get Answer"):
        response = openai.Completion.create(
            model="gpt-4",
            prompt=question,
            max_tokens=100
        )
        answer = response.choices[0].text.strip()
        st.write(f"Answer: {answer}")

from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env file

import streamlit as st
import os
import google.generativeai as genai

# Configure the Gemini API using the API key from the environment variable
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load Gemini model and get a response
model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])  # Empty history for each new session

# Function to get a response from the Gemini model for football injury rehab questions
def get_gemini_response(question):
    # Create a prompt that ensures the response is focused on football injury rehab
    football_prompt = (
        "You are a highly specialized rehabilitation assistant for football players. "
        "Provide detailed advice for recovery, rehabilitation exercises, and injury management. "
        "Question: " + question
    )
    
    # Get a response from the model with the specialized prompt
    response = chat.send_message(football_prompt, stream=True)
    return response

# Initialize Streamlit app settings
st.set_page_config(page_title="Football Injury Rehab Chatbot")

st.header("Football Injury Rehab Assistant")

# Input box for user to ask football injury-related questions
input_question = st.text_input("Ask your football injury rehab question:")

# Submit button to send the question
submit = st.button("Ask the question")

if submit and input_question:
    # Get the response from the Gemini model
    response = get_gemini_response(input_question)

    # Display the response
    st.subheader("Rehabilitation Advice")
    for chunk in response:
        st.write(chunk.text)

# Instruction message
st.info("Ask any question related to football injuries and rehab strategies. This chatbot provides advice on treatments, exercises, and recovery plans.")
     
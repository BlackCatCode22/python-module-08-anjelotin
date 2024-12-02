# ChatBotApp.py
# Starter code for Python Chat Bot Program
#CIT-95 (Mohle) Spring 2024
# last updated: 11/1/24 by Angelo Andrade
#Suggested things to do:
# Add chat memory
#Use a local server like streamlit
# Modify streamlit with HTML to make a nice looking chat bot
# Use Langchain framework to read .pdf files
#Use an open source LLH that doesn't cost tokens
# pip install this dependency if you don't have this already
#pip install openai
import openai
import streamlit as st

# Fetch the OpenAI API key from Streamlit secrets
openai.api_key = st.secrets["OPENAI_API_KEY"]

def generate_response(user_input):
    try:
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": "Assume the role of a Python teacher, and think step by step. Your name is Skippy Py."},
                      {"role": "user", "content": user_input}]
        )

        response_text = completion['choices'][0]['message']['content']
        return response_text
    except Exception as e:
        print("Error generating response:", e)
        return "I'm sorry, I couldn't generate a response."

def main():
    # Set up the Streamlit interface
    st.title("Python Study Bot")
    st.write("Welcome! Ask your Python questions below. Type 'quit' to exit.")

    # Text input for the user
    user_input = st.text_input("Python student question:")

    if user_input:
        if user_input.lower() == "quit":
            st.write("exit")
        else:
            response = generate_response(user_input)
            st.write("Python Study Bot:", response)

if __name__ == "__main__":
    main()
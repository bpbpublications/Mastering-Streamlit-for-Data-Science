import streamlit as st
import requests

# Function to fetch random quotes from an online API
def fetch_random_quote():
    response = requests.get('https://api.quotable.io/random')
    if response.status_code == 200:
        data = response.json()
        return f"{data['content']} - {data['author']}"
    else:
        return "Unable to fetch quote at this time."

# Chat interface in Streamlit
st.title("Random Quote Chatbot")
user_input = st.chat_input("Send a message to the chatbot")

if user_input:
    with st.chat_message('user'):
        st.write(user_input)
    with st.chat_message('assistant'):
       st.write(fetch_random_quote())
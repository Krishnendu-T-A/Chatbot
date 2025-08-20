import datetime
import streamlit as st
from chatbot.bot import ChatBot
from chatbot.utils import setup_nltk

def main():
    setup_nltk()
    bot = ChatBot()

    st.title("Chatbot 🤖")
    current_hour = datetime.datetime.now().hour
    if current_hour < 12:
        greeting = "Good morning! ☀️"
    elif current_hour < 18:
        greeting = "Good afternoon! 😊"
    else:
        greeting = "Good evening! 🌙"

    st.write(f"{greeting} Welcome to the chatbot. Type a message and press Enter to start the conversation.")

    user_input = st.text_input("You:", key="user_input")

    if user_input:
        response = bot.get_response(user_input)
        st.text_area("Chatbot:", value=response, height=100, key="chatbot_response")

        if response.lower() in ['goodbye', 'bye']:
            st.write("Thank you for chatting with me. Have a great day! 👋")
            st.stop()

if __name__ == '__main__':
    main()

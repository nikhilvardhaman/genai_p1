import streamlit as st
import openai
from openai import OpenAI
import os

# if os.getenv('openai_apikey'):
#     openai_api_key = os.getenv('openai_apikey')
# else:
#    openai_api_key = st.secrets['DB_TOKEN']

# import streamlit as st

# st.write("DB username:", st.secrets["db_username"])
# st.write("DB password:", st.secrets["db_password"])


client = OpenAI(api_key=st.secrets["db_password"])

def generate_grammar_exercise():
    completion = client.chat.completions.create(
      model="gpt-4o-mini",
      messages=[
      {"role": "system", "content": "You are a language teacher. your job is to teach people english grammar, via fun and interesting short exercises by sharing with them some fill in the blanks or multiple choice questions. Please give one question only"},
      {"role": "user", "content": "Create a fun grammar exercise (fill in the blanks or multiple choice) based on English language. Please give one question only"}
      ]
    )
    print(completion.choices[0].message.content)
    return completion.choices[0].message.content.strip()

    
def check_answer(question, user_answer):
    # Using OpenAI to check the user's answer and provide feedback
    completion = client.chat.completions.create(
      model="gpt-4o-mini",
      messages=[
      {"role": "system", "content": "You are a language teacher. your job is to teach people english grammar. you will be give a question and an answer, both by the user. you have to evaluate it and share feedback. please be supportive and helpful."},
      {"role": "user", "content": f"Question: {question}\nAnswer: {user_answer}\nEvaluate the correctness of the answer and provide feedback:"}
      ]
    )
    print(completion.choices[0].message.content)
    return completion.choices[0].message.content.strip()


def app():
    st.title('Grammar Tutor')
    st.write('Welcome to the Grammar Tutor app! Sharpen your grammar skills with these exercises.')

    # State management for exercise generation and user input
    if 'exercise' not in st.session_state:
        st.session_state.exercise = None
    if 'user_response' not in st.session_state:
        st.session_state.user_response = ''

    # Generate exercise button
    if st.button('Start'):
        st.session_state.exercise = generate_grammar_exercise()
    
    if st.session_state.exercise:
        st.subheader('Exercise:')
        st.write(st.session_state.exercise)

        # User input for response
        user_response = st.text_input('Your answer:', key="response")

        if st.button('Check Answer'):
            if user_response:
                st.session_state.user_response = user_response
                feedback = check_answer(st.session_state.exercise, st.session_state.user_response)
                st.subheader('Feedback on Your Answer:')
                st.write(feedback)
            else:
                st.error("Please enter an answer before checking.")
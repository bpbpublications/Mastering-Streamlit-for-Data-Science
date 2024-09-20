import streamlit as st
import random

if st.checkbox("Stop the app"):
    st.write("App stopped.")
    st.stop()

st.write("This will not be displayed if the checkbox is checked.")

if st.button("Rerun the app"):
    st.rerun()

st.write(random.randint(1, 100))  # Display a random number

with st.form(key='my_form'):
    text_input = st.text_input(label='Enter some text')
    submit_button = st.form_submit_button(label='Submit')

if submit_button:
    st.write(f'You entered: {text_input}')


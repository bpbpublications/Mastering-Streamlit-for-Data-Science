import streamlit as st

# Callback to process form submission
def process_form():
    user_name = st.session_state.user_name
    user_age = st.session_state.user_age
    st.write(f"Name: {user_name}, Age: {user_age}")

# Define a form with inputs and a submit button
with st.form("user_form", clear_on_submit=True):
    st.text_input("Enter your name", key="user_name")
    st.number_input("Enter your age", min_value=0, max_value=100, step=1, key="user_age")
    submit_button = st.form_submit_button("Submit", on_click=process_form)

# Optional: Display session state (for debugging purposes)
# st.write(st.session_state)

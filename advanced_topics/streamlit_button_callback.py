import streamlit as st

# Define the callback function
def toggle_message():
    if 'show_message' not in st.session_state:
        st.session_state.show_message = False
    st.session_state.show_message = not st.session_state.show_message

# Create a button and associate the callback
st.button("Toggle Message", on_click=toggle_message)

# Conditional display based on the callback's effect on session state
if st.session_state.get('show_message', False):
    st.write("Hello, Streamlit!")

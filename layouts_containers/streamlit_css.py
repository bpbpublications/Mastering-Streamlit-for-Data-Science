import streamlit as st

# Inject custom CSS with st.markdown
st.markdown("""
    <style>
    .main-title {
        color: blue;
        font-family: Arial, sans-serif;
    }

    .custom-text {
        color: green;
        font-size: 20px;
    }

    /* Style the Streamlit elements */
    .stTextInput > label, .stButton > button {
        color: red;
    }
    </style>
    """, unsafe_allow_html=True)

# Use the custom CSS classes
st.markdown('<h1 class="main-title">Custom CSS Title</h1>', unsafe_allow_html=True)
st.markdown('<p class="custom-text">This text has custom CSS applied to it.</p>', unsafe_allow_html=True)

# Standard Streamlit elements
st.text_input("This input label is styled with custom CSS")
st.button("This button's text is styled with custom CSS")

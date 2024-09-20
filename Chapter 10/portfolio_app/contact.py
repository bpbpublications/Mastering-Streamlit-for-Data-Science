import streamlit as st

def contact_show():

    st.title('Contact Me')

    with st.form(key='contact_form'):
        name = st.text_input('Name')
        email = st.text_input('Email')
        message = st.text_area('Message')
        submit_button = st.form_submit_button('Send')

        if submit_button:
            if len(name) < 2:
                st.warning('Name too short.')
            elif '@' not in email:
                st.warning('Please enter a valid email address.')
            else:
                st.success('Thanks for your message!')

    col1, col2, col3,col4 , col5 = st.columns(5)
    with col3:

        st.markdown(
            "[LinkedIn](https://www.linkedin.com/in/johnturner)[|Twitter|](https://www.twitter.com/johnturner) [GitHub](https://www.github.com/johnturner) [|Instagram](https://www.instagram.com/johnturner)")

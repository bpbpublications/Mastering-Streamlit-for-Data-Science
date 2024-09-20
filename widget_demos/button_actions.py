import streamlit as st

st.button("Reset", type="primary")
if st.button('Say Good morning'):
    st.write('Good Morning ')
else:
    st.write('Good Evening')

st.divider()

#download the string as a file
text_contents = '''This is some text'''
st.download_button('Download some text', text_contents)

st.divider()

st.link_button("Go to gallery", "https://streamlit.io/gallery")
import streamlit as st

st.title('Data Counter')
number = st.number_input('Enter the count', value=0, step=1)
if st.button('Add More Count'):
    st.write('Total count:', number)

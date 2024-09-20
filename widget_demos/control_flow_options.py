import streamlit as st


if "value" not in st.session_state:
    st.session_state.value = "Title"

##### Option using st.rerun #####
st.header(st.session_state.value)

if st.button("Foo"):
    st.session_state.value = "Foo"
    st.rerun()


# #stop the execution
# fruit = st.text_input('What is your favourite fruit ?')
# if not fruit:
#   st.write('Please input a fruit')
#   st.stop()
#   st.write('Or a vegetable (this will not be printed)')
#
# st.write(f'My favourite fruit is {fruit} too !!')
#

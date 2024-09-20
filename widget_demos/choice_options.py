import streamlit as st

#multiple input select

options = st.multiselect(
    'What are your favorite colors',
    ['Green', 'Yellow', 'Red', 'Blue'],
    ['Yellow','Red'])

st.write('You selected:', options)

st.divider()

start_color, end_color = st.select_slider(
    'Select a range of color wavelength',
    options=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'],
    value=('red', 'blue'))
st.write('You selected wavelengths between', start_color, 'and', end_color)
#
# #single input select
# agree = st.checkbox('I agree')
# # checkbox returns true/false
# if agree:
#     st.write('You have agreed!')
#
# st.divider()
#
# on = st.toggle('Activate feature')
# # toggle returns true/false
# if on:
#     st.write('Feature activated!')
#
# st.divider()
#
# color = st.radio(
#     "What's your favorite Color",
#     [":rainbow[Rainbow]", "Black"],
#     captions = ["All the colors in Rainbow", "Black rules"])
# # The application can behave as per selection made in the radio button
# if color == ':rainbow[Rainbow]':
#     st.write('You selected rainbow.')
# else:
#     st.write("You didn\'t select rainbow.")
#
# st.divider()
#
# option = st.selectbox(
#    "How would you like to be contacted?",
#    ("Email", "Home phone", "Mobile phone"),
#    index=None,
#    placeholder="Select contact method...",
# )
#
# st.write('You selected:', option)
#
# st.divider()
#
# age = st.slider('How old are you?', 0, 130, 25)
# st.write("I'm ", age, 'years old')
#

import streamlit as st
import time
#
# # Create a progress bar
# # progress_bar = st.progress(0)
# # for percent_complete in range(100):
# #     time.sleep(0.1)
# #     progress_bar.progress(percent_complete + 1)
# #
# # st.divider()
# # #
# # with st.spinner('Wait for it...'):
# #     time.sleep(5)
#
#
# st.divider()
# # Display different status messages
# st.error('This is an error message')
# st.warning('This is a warning message')
# st.info('This is an informational message')
# st.success('This is a success message')
st.divider()
if st.button('Celebrate with ballons!'):
    st.balloons()
st.divider()
if st.button('Celebrate with snow!'):
    st.snow()
st.divider()
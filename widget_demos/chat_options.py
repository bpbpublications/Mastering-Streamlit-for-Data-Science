import streamlit as st
import numpy as np

with st.chat_message("user",avatar= '🤖'):
    st.write("Hello 👋")
    st.line_chart(np.random.randn(30, 3))
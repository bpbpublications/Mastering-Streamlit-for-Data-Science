import streamlit as st
from joblib import load

# Load the model
model = load('/Users/surabhi/PycharmProjects/streamlit_github/ml_model_integration/linear_regression_model.joblib')


st.title('Exam Score Prediction Based on Hours Studied')

hours_studied = st.slider('Hours Studied', min_value=1, max_value=10, value=5)


predicted_score = model.predict([[hours_studied]])[0]
st.write(f'Predicted Exam Score: {predicted_score:.2f}')

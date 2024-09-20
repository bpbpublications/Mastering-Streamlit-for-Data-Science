import streamlit as st
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import make_classification
from sklearn.metrics import accuracy_score

# Set page title
st.title("Logistic Regression Model")

# Generate a synthetic dataset
X, y = make_classification(n_samples=100, n_features=2, n_informative=2, n_redundant=0, random_state=42)

# Create interactive controls
C = st.slider("Regularization strength", min_value=0.01, max_value=1.0, value=0.5, step=0.01)
penalty = st.selectbox("Penalty", options=["l2", "l1", "elasticnet", "none"])

# Train the model based on user-selected parameters
model = LogisticRegression(C=C, penalty=penalty, solver='saga', l1_ratio=0.5 if penalty == 'elasticnet' else None)
model.fit(X, y)

# Predict and calculate accuracy
predictions = model.predict(X)
accuracy = accuracy_score(y, predictions)

# Display the accuracy
st.write(f"Model accuracy: {accuracy:.2f}")
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pandas as pd
from joblib import dump

# Sample dataset
data = {
    'Hours_Studied': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Exam_Score': [51, 55, 60, 68, 72, 75, 78, 82, 88, 90]
}

df = pd.DataFrame(data)

# Preparing the data
X = df[['Hours_Studied']]  # Predictor
y = df['Exam_Score']  # Response

# Splitting dataset into training and testing set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Training the model
model = LinearRegression()
model.fit(X_train, y_train)

dump(model, 'linear_regression_model.joblib')
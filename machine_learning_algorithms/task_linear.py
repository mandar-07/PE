import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
import numpy as np

# Load data
df = pd.read_csv("housing.csv")
print("Missing values:", df.isnull().sum().sum())

# Features & Target
X = df[["RM", "LSTAT", "PTRATIO"]]  # independent variables
y = df["MEDV"]                      # dependent variable

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluation metrics
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Predicting a sample
sample = pd.DataFrame({"RM": [7.0], "LSTAT": [5.0], "PTRATIO": [15.0]})
prediction = model.predict(sample)

# Output
print("Predicted MEDV for sample:", prediction[0])
print("Mean Squared Error:", mse)
print("R² Score (Accuracy):", r2)

import pandas as pd 
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
import numpy as np

# Load data
df = pd.read_csv("housing.csv")
print("Missing values:", df.isnull().sum().sum())

# Features & Target
X = df[["RM", "LSTAT", "PTRATIO"]]
y = df["MEDV"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Grid Search for best hyperparameters
param_grid = {
    'max_depth': [3, 5, 10, None],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4]
}

grid_search = GridSearchCV(DecisionTreeRegressor(random_state=42), param_grid, cv=5, scoring='r2')
grid_search.fit(X_train, y_train)

# Best model from GridSearchCV
best_model = grid_search.best_estimator_

# Prediction & Evaluation
y_pred = best_model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Predict a custom sample
sample = pd.DataFrame({"RM": [7.0], "LSTAT": [5.0], "PTRATIO": [15.0]})
prediction = best_model.predict(sample)

# Output
print("Best Hyperparameters:", grid_search.best_params_)
print("Predicted MEDV for sample:", prediction[0])
print("Mean Squared Error:", mse)
print("R² Score (Accuracy):", r2)

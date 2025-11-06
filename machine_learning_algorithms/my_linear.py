import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt


model = LinearRegression()







data_frame=pd.read_csv("gld_price_data.csv")

print(data_frame)
print(data_frame.isnull().sum().sum())



Y= data_frame["GLD"]
X = data_frame.drop(["GLD", "Date"], axis=1)


X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
model.fit(X_train, Y_train)
y_pred = model.predict(X_test)
print(y_pred)
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
import numpy as np


r2 = r2_score(Y_test, y_pred)
mse = mean_squared_error(Y_test, y_pred)
rmse = np.sqrt(mse)
mae = mean_absolute_error(Y_test, y_pred)

print("R² Score:", r2)
print("Mean Squared Error:", mse)
print("Root Mean Squared Error:", rmse)
print("Mean Absolute Error:", mae)

plt.figure(figsize=(8,6))
plt.scatter(Y_test, y_pred, color='blue')
plt.xlabel("Actual Gold Price")
plt.ylabel("Predicted Gold Price")
plt.title("Actual vs Predicted Gold Price")
plt.show()

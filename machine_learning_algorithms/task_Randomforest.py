import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
import numpy as np


df=pd.read_csv("housing.csv")
df.isnull().sum().sum()
print("missing values:",df.isnull().sum().sum())

X = df[["RM", "LSTAT", "PTRATIO"]] #independent variable 
y = df["MEDV"]  # dependent variable


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)


y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)
r2 = r2_score(y_test, y_pred)


sample = pd.DataFrame({"RM": [7.0], "LSTAT": [5.0], "PTRATIO": [15.0]})
prediction = model.predict(sample)
print("Predicted MEDV for sample:", prediction[0])
print("acurracy",r2)
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
import numpy as np

# Sample data
data = {
    "name": ["Mandar", "Aryan", "Pruthviraj", "soham", "harsh", "Anup", "Sumedh", "Swayam", "Shiv", "Ary"],
    "Weight": [60, 53, 55, 65, 45, 65, 60, 52, 58, 57],
    # Let's assume 1 = Fit, 0 = Not Fit (this is just made-up logic)
    "Fit":     [1,   0,   0,   1,  0,   1,    1,    0,   1,   0]
}
df = pd.DataFrame(data)

# Features and target
X = df[["Weight"]]
y = df["Fit"]

# Create logistic regression model
model = LogisticRegression()
model.fit(X, y)

# Generate weight range for smooth curve
weight_range = np.linspace(df["Weight"].min(), df["Weight"].max(), 300).reshape(-1,1)
predicted_probs = model.predict_proba(weight_range)[:, 1]

# Plot
plt.figure(figsize=(10,6))
plt.scatter(df["Weight"], df["Fit"], color='red', label="Actual Data")
plt.plot(weight_range, predicted_probs, color='blue', label="Logistic Regression Curve")
plt.xlabel("Weight (kg)")
plt.ylabel("Probability of Being Fit")
plt.title("Logistic Regression - Weight vs Fit")
plt.legend()
plt.grid(True)
plt.show()

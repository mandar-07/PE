import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier

# Load data
train_df = pd.read_csv("train1.csv")
test_df = pd.read_csv("test.csv")

# Map gender: Male = 1, Female = 0
train_df['gender'] = train_df['gender'].map({'Male': 1, 'Female': 0})

# Drop unnecessary columns
train_df.drop(['native-country', 'income_>50K'], axis=1, inplace=True)
test_df.drop(['native-country'], axis=1, inplace=True)

# Combine for label encoding
combined = pd.concat([train_df.drop('gender', axis=1), test_df], axis=0)

# Encode categorical columns
label_encoders = {}
for col in combined.select_dtypes(include='object').columns:
    le = LabelEncoder()
    combined[col] = le.fit_transform(combined[col])
    label_encoders[col] = le

# Split back
X_train = combined[:len(train_df)]
X_test = combined[len(train_df):]
y_train = train_df['gender']

# Train model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Predict on test data
predictions = model.predict(X_test)

# Add predictions to test_df
test_df['predicted_gender'] = predictions

# Save to CSV (optional)
test_df.to_csv("gender_predictions.csv", index=False)

print(test_df[['age', 'predicted_gender']].head())

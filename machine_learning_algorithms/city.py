import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score

# === Load Dataset ===
df = pd.read_csv('data1.csv')

# === Check for Missing Values ===
print("🔎 Missing values per column:\n", df.isnull().sum())
print("\n⚠️ Columns with missing values:", list(df.columns[df.isnull().any()]))

# === Drop Unnecessary Columns ===
df.drop(columns=['street'], inplace=True)

# === Handle Missing Values ===
# Fill numeric columns with mean
df.fillna(df.mean(numeric_only=True), inplace=True)

# Fill categorical columns with mode (safe syntax)
for col in df.select_dtypes(include=['object']).columns:
    df[col] = df[col].fillna(df[col].mode()[0])

# === Parse Date Column ===
df['date'] = pd.to_datetime(df['date'])
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month
df.drop(columns=['date'], inplace=True)

# === Encode Target Columns ===
le_city = LabelEncoder()
le_country = LabelEncoder()
df['city'] = le_city.fit_transform(df['city'])
df['country'] = le_country.fit_transform(df['country'])

# === Check Unique Classes Before Training ===
print("\nUnique 'country' values:", df['country'].unique())
print("Class distribution:\n", df['country'].value_counts())

# === Separate Features and Targets ===
features = df.drop(columns=['city', 'country'])
target_city = df['city']
target_country = df['country']

# === Encode All Categorical Features ===
for col in features.columns:
    if features[col].dtype == 'object':
        features[col] = LabelEncoder().fit_transform(features[col])

# === Scale Features ===
scaler = StandardScaler()
features_scaled = scaler.fit_transform(features)

# === Train-Test Splits ===
X_train_c, X_test_c, y_train_c, y_test_c = train_test_split(features_scaled, target_city, test_size=0.2, random_state=42)
X_train_cn, X_test_cn, y_train_cn, y_test_cn = train_test_split(features_scaled, target_country, test_size=0.2, random_state=42)

# === Logistic Regression Model ===
model = LogisticRegression(max_iter=1000)

# === Function to Train and Evaluate ===
def train_and_evaluate(X_train, X_test, y_train, y_test, label):
    print(f"\n=== Logistic Regression Results for predicting {label} ===")
    model.fit(X_train, y_train)
    preds = model.predict(X_test)
    print("Accuracy:", accuracy_score(y_test, preds))
    print(classification_report(y_test, preds))

# === Run for Country Prediction (if valid) ===
if df['country'].nunique() < 2:
    print("\n⚠️ Skipping 'country' model training because it has only one class.")
else:
    train_and_evaluate(X_train_cn, X_test_cn, y_train_cn, y_test_cn, label="Country")

# === Run for City Prediction ===
train_and_evaluate(X_train_c, X_test_c, y_train_c, y_test_c, label="City")

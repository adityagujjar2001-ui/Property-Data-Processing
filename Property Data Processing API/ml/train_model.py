import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from ml.features import get_feature_matrix

# Load dataset
df = pd.read_csv("data/sample_properties.csv")

# Features & target
X = get_feature_matrix(df)
y = df["price"]

# Preprocessing
categorical_features = ["city"]
numeric_features = ["area", "bedrooms", "bathrooms"]

preprocessor = ColumnTransformer(
    transformers=[
        ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features)
    ],
    remainder="passthrough"
)

# Model pipeline
model = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("regressor", RandomForestRegressor(n_estimators=100, random_state=42))
])

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train
model.fit(X_train, y_train)

# Save model
with open("ml/model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model trained and saved successfully!")
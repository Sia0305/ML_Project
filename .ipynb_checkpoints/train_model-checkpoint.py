import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

# Load dataset
df = pd.read_csv("cardio_train.csv", sep=";")

# Remove id because it is not useful for prediction
df = df.drop("id", axis=1)

# Features
X = df.drop("cardio", axis=1)

# Target
y = df["cardio"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Model pipeline
model = Pipeline([
    ("scaler", StandardScaler()),
    ("classifier", LogisticRegression(max_iter=1000))
])

# Train
model.fit(X_train, y_train)

# Save model
joblib.dump(model, "cardio_model.pkl")

print("Model trained successfully!")
print("Model saved as cardio_model.pkl")
import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Load dataset
df = pd.read_csv("phishing_dataset/malicious_phish.csv")

# Use sample for faster training
df = df.sample(20000, random_state=42)

# Convert labels
df["label"] = df["type"].apply(
    lambda x: 0 if x == "benign" else 1
)

X = df["url"]
y = df["label"]

# TF-IDF
vectorizer = TfidfVectorizer(max_features=5000)

X = vectorizer.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Deep Learning Model
model = Sequential([
    Dense(128, activation="relu", input_shape=(5000,)),
    Dense(64, activation="relu"),
    Dense(1, activation="sigmoid")
])

model.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["accuracy"]
)

print("Training Deep Learning Model...")

model.fit(
    X_train.toarray(),
    y_train,
    epochs=5,
    batch_size=32
)

loss, accuracy = model.evaluate(
    X_test.toarray(),
    y_test
)

print("Accuracy:", accuracy)

# Save model
model.save("dl_phishing_model.keras")

# Save vectorizer
joblib.dump(
    vectorizer,
    "dl_vectorizer.pkl"
)

print("Deep Learning Model Saved")
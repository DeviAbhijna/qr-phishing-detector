import joblib

from tensorflow.keras.models import load_model

model = load_model(
    "dl_phishing_model.keras"
)

vectorizer = joblib.load(
    "dl_vectorizer.pkl"
)

def predict_dl(url):

    X = vectorizer.transform([url])

    prediction = model.predict(
        X.toarray()
    )[0][0]

    if prediction > 0.5:
        return "Malicious"

    return "Benign"
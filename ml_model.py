import joblib

model = joblib.load("phishing_model.pkl")

def predict_url(url):
    prediction = model.predict([url])[0]
    return prediction
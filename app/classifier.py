import joblib
model = joblib.load("models/emotion_model.pkl")
vectorizer = joblib.load("models/vectorizer.pkl")

def predict_emotion(text):
    X_vec = vectorizer.transform([text])
    prediction = model.predict(X_vec)[0]
    return prediction
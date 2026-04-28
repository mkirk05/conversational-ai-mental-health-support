import pandas as pd
import joblib

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

#Load dataset
data = pd.read_csv("data/train_dataset.csv")
data = data.dropna(subset=["text", "label"])

X = data["text"]
Y = data["label"]

#Vectorize text
vectorizer = TfidfVectorizer()
X_vec = vectorizer.fit_transform(X)

#Train model
model = LogisticRegression(max_iter=1000)
model.fit(X_vec, Y)

# Save model + vectorizer
joblib.dump(model, "models/emotion_model.pkl")
joblib.dump(vectorizer, "models/vectorizer.pkl")

print("Model trained and saved.")
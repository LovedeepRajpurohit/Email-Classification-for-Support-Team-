import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import pandas as pd

# Load or Train the Model
def train_and_save_model():
    # Load dataset
    data = pd.read_csv("data/combined_emails_with_natural_pii.csv")
    texts = data['email_body']
    labels = data['category']

    # Vectorize the text data
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(texts)

    # Train the Naive Bayes classifier
    model = MultinomialNB()
    model.fit(X, labels)

    # Save model and vectorizer
    with open("models/classifier.pkl", "wb") as f:
        pickle.dump((model, vectorizer), f)

def classify_email(email_body: str) -> str:
    # Load the pre-trained model and vectorizer
    with open("models/classifier.pkl", "rb") as f:
        model, vectorizer = pickle.load(f)

    # Transform the input email body
    X = vectorizer.transform([email_body])

    # Predict the category
    category = model.predict(X)[0]
    return category
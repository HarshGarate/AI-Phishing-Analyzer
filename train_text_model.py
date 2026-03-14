import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
import joblib
import os

print("Creating text training data...")
# A small dummy dataset of emails/messages (0 = Safe, 1 = Phishing)
data = {
    'text': [
        "Hey, are we still on for lunch tomorrow at 12?",
        "URGENT: Your bank account has been locked. Click here to verify your identity.",
        "Please review the attached invoice for your recent purchase.",
        "Your password will expire in 24 hours. Reset it immediately using this link.",
        "Happy birthday! Hope you have a fantastic day.",
        "Security Alert: Unauthorized login attempt detected. Secure your account now.",
        "Can you send me the project files by end of day?",
        "Congratulations! You've won a $1000 gift card. Claim your prize here."
    ],
    'label': [0, 1, 0, 1, 0, 1, 0, 1]
}
df = pd.DataFrame(data)

# Create an NLP pipeline: 
# 1. TfidfVectorizer converts the text into a matrix of word frequencies.
# 2. MultinomialNB (Naive Bayes) learns which words indicate phishing.
print("Training Naive Bayes NLP model...")
model = make_pipeline(TfidfVectorizer(), MultinomialNB())

# Train the model
model.fit(df['text'], df['label'])

# Save the model
print("Saving text model to 'models' folder...")
os.makedirs('models', exist_ok=True)
joblib.dump(model, 'models/text_nb_model.pkl')

print("Success! text_nb_model.pkl is ready for Streamlit.")
import random
from textblob import TextBlob
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from .intents import INTENTS

class ChatBot:
    def __init__(self):
        self.intents = INTENTS
        self.vectorizer = TfidfVectorizer()
        self.classifier = LogisticRegression(random_state=0, max_iter=10000)
        self.memory = ""  # To store last user input
        self.train_model()

    def train_model(self):
        """Train the chatbot model"""
        patterns, tags = [], []
        for intent in self.intents:
            for pattern in intent['patterns']:
                patterns.append(pattern)
                tags.append(intent['tag'])

        X = self.vectorizer.fit_transform(patterns)
        y = tags
        self.classifier.fit(X, y)

    def get_response(self, user_input):
        """Generate chatbot response"""
        self.memory = user_input
        sentiment = TextBlob(user_input).sentiment.polarity

        if sentiment > 0:
            sentiment_response = "You seem happy! 😊 "
        elif sentiment < 0:
            sentiment_response = "Oh, that sounds tough. 😟 "
        else:
            sentiment_response = ""

        try:
            X_input = self.vectorizer.transform([user_input])
            predicted_tag = self.classifier.predict(X_input)[0]
        except:
            predicted_tag = "fallback"

        for intent in self.intents:
            if intent['tag'] == predicted_tag:
                return sentiment_response + random.choice(intent['responses'])

        return "I'm sorry, I didn't understand that."

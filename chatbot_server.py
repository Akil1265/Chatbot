from flask import send_from_directory
import os
from flask import Flask, request, jsonify
import random
import json
import nltk
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

nltk.download('punkt')
nltk.download('wordnet')

lemmatizer = WordNetLemmatizer()

# Load intents
with open("intents.json", encoding="utf-8") as file:
    data = json.load(file)

corpus = []
labels = []
for intent in data["intents"]:
    for pattern in intent["patterns"]:
        tokens = nltk.word_tokenize(pattern.lower())
        lemmas = [lemmatizer.lemmatize(word) for word in tokens]
        corpus.append(" ".join(lemmas))
        labels.append(intent["tag"])

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(corpus)
classifier = MultinomialNB()
classifier.fit(X, labels)


def predict_intent(user_input):
    tokens = nltk.word_tokenize(user_input.lower())
    lemmas = [lemmatizer.lemmatize(word) for word in tokens]
    input_vec = vectorizer.transform([" ".join(lemmas)])
    prediction = classifier.predict(input_vec)[0]
    return prediction


def get_response(tag):
    for intent in data["intents"]:
        if intent["tag"] == tag:
            return random.choice(intent["responses"])


app = Flask(__name__)


@app.route('/')
def index():
    return send_from_directory(os.path.dirname(os.path.abspath(__file__)), 'chatbot.html')


@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    intent = predict_intent(user_input)
    response = get_response(intent)
    return jsonify({'response': response})


if __name__ == '__main__':
    app.run(debug=True)

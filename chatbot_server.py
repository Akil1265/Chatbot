from flask import Flask, request, jsonify, send_from_directory
import os
import json
import random
import nltk
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Ensure NLTK resources are available
def ensure_nltk_resources():
    resources = ['punkt_tab', 'wordnet']
    for resource in resources:
        try:
            if resource == 'punkt_tab':
                nltk.data.find('tokenizers/punkt_tab/english/')
            else:
                nltk.data.find('corpora/wordnet')
        except LookupError:
            nltk.download(resource, quiet=True)

ensure_nltk_resources()

# Initialize components
lemmatizer = WordNetLemmatizer()

# Load intents and train model
with open("intents.json", encoding="utf-8") as file:
    data = json.load(file)

# Prepare training data
corpus = []
labels = []
for intent in data["intents"]:
    for pattern in intent["patterns"]:
        tokens = nltk.word_tokenize(pattern.lower())
        lemmas = [lemmatizer.lemmatize(word) for word in tokens]
        corpus.append(" ".join(lemmas))
        labels.append(intent["tag"])

# Train model
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(corpus)
classifier = MultinomialNB()
classifier.fit(X, labels)

def predict_intent(user_input):
    tokens = nltk.word_tokenize(user_input.lower())
    lemmas = [lemmatizer.lemmatize(word) for word in tokens]
    input_vec = vectorizer.transform([" ".join(lemmas)])
    return classifier.predict(input_vec)[0]

def get_response(tag):
    for intent in data["intents"]:
        if intent["tag"] == tag:
            return random.choice(intent["responses"])
    return "Sorry, I didn't understand that. Can you rephrase?"


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
    print('Starting Flask app...')
    print('Open your browser to: http://127.0.0.1:5000')
    try:
        # Disable the reloader to keep a single process and make output deterministic
        app.run(host='127.0.0.1', port=5000, debug=True, use_reloader=False)
    except Exception as e:
        print(f'Error while running Flask app: {e}')
        exit(1)

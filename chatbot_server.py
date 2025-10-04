import traceback
import sys
print('Starting chatbot_server: importing modules...')
try:
    from flask import send_from_directory
    import os
    from flask import Flask, request, jsonify
    import random
    import json
    import nltk
    from nltk.stem import WordNetLemmatizer
    from sklearn.feature_extraction.text import CountVectorizer
    from sklearn.naive_bayes import MultinomialNB

    def ensure_nltk_resources():
        """Ensure required NLTK resources are available; download quietly if missing."""
        resources = {
            'punkt': 'tokenizers/punkt',
            'wordnet': 'corpora/wordnet'
        }
        for name, path in resources.items():
            try:
                nltk.data.find(path)
            except LookupError:
                print(f"NLTK resource '{name}' not found; downloading...")
                nltk.download(name, quiet=True)

    ensure_nltk_resources()
    print('Modules imported and NLTK resources ensured.')
except Exception:
    print('Error during imports or NLTK setup:')
    traceback.print_exc()
    sys.exit(1)

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
    # Fallback if no intent matches
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
    try:
        # Disable the reloader to keep a single process and make output deterministic
        app.run(host='127.0.0.1', port=5000, debug=True, use_reloader=False)
    except Exception:
        print('Error while running Flask app:')
        traceback.print_exc()
        sys.exit(1)

import random
import json
import nltk
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

nltk.download('punkt')
nltk.download('wordnet')

lemmatizer = WordNetLemmatizer()


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
    # If no intent matches, return a default response
    return "Sorry, I didn't understand that. Can you rephrase?"


print("Bot: Hello! How can I assist you today? (Type 'quit' to exit)")
while True:
    user_input = input("You: ").strip()
    if not user_input:
        continue
    if user_input.lower() == "quit":
        print("Bot: Goodbye! Have a wonderful day! 😊")
        break
    intent = predict_intent(user_input)
    response = get_response(intent)
    if not response:
        response = "Sorry, I didn't understand that. Can you rephrase?"
    print("Bot: ", response)

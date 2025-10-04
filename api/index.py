from flask import Flask, request, jsonify, send_from_directory
import os
import json
import random

# Load intents from parent directory
intents_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'intents.json')
with open(intents_path, encoding="utf-8") as file:
    data = json.load(file)

def predict_intent(user_input):
    """Simple keyword-based intent prediction for Vercel deployment"""
    user_input = user_input.lower()
    
    # Check for greetings
    if any(word in user_input for word in ['hi', 'hello', 'hey', 'good morning', 'good evening']):
        return "greeting"
    
    # Check for goodbye
    if any(word in user_input for word in ['bye', 'goodbye', 'see you']):
        return "goodbye"
    
    # Check for thanks
    if any(word in user_input for word in ['thanks', 'thank you', 'helpful']):
        return "thanks"
    
    # Check for help
    if any(word in user_input for word in ['help', 'what can you do']):
        return "help"
    
    # Check for jokes
    if any(word in user_input for word in ['joke', 'funny', 'laugh']):
        return "joke"
    
    # Check for name
    if any(word in user_input for word in ['name', 'who are you']):
        return "name"
    
    # Check for age
    if any(word in user_input for word in ['age', 'old']):
        return "age"
    
    # Check for feeling
    if any(word in user_input for word in ['how are you', 'feeling', 'okay']):
        return "feeling"
    
    # Default to unknown
    return "unknown"

def get_response(tag):
    for intent in data["intents"]:
        if intent["tag"] == tag:
            return random.choice(intent["responses"])
    return "Sorry, I didn't understand that. Can you rephrase?"

app = Flask(__name__)

@app.route('/')
def index():
    html_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'chatbot.html')
    return send_from_directory(os.path.dirname(html_path), 'chatbot.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    intent = predict_intent(user_input)
    response = get_response(intent)
    return jsonify({'response': response})

# Vercel handler
def handler(request):
    return app(request.environ, lambda status, headers: None)
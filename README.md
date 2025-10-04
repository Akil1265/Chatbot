# Chatbot

AI-powered chatbot using Flask web server and machine learning for natural language processing.

## Quick Start

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the server:
```bash
python chatbot_server.py
```

3. Open http://127.0.0.1:5000 in your browser

## Features
- Web-based chat interface
- Machine learning intent classification
- Natural language processing with NLTK
- Multiple response variations for each intent

## Machine Learning Models & Libraries

### 🧠 ML Models Used
- **Algorithm**: Naive Bayes (MultinomialNB) from scikit-learn 1.7.2
- **Text Vectorization**: CountVectorizer (Bag of Words)
- **Intent Classification**: Probabilistic text classifier

### 🔤 Natural Language Processing
- **NLTK 3.9.2** with:
  - punkt_tab tokenizer (text splitting)
  - WordNet lemmatizer (word normalization)

### 🌐 Web Framework
- **Flask 3.1.2**: Web server
- **Jinja2 3.1.6**: HTML templating
- **Werkzeug 3.1.3**: WSGI utilities

### 📊 Supporting Libraries
- **NumPy 2.3.3**: Numerical computations
- **SciPy 1.16.2**: Scientific computing
- **joblib 1.5.2**: Parallel processing

### 🎯 How It Works
1. User input → NLTK tokenization
2. Text normalization → Lemmatization
3. Feature extraction → CountVectorizer
4. Intent prediction → Naive Bayes
5. Response selection → Random from intents.json

## Files
- `chatbot_server.py` - Flask web server with ML pipeline
- `chatbot.py` - Command-line version
- `chatbot.html` - Modern web interface
- `intents.json` - Training data and responses
- `requirements.txt` - All dependencies

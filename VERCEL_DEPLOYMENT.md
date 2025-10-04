# Vercel Deployment Guide

## 🚀 Ready for Vercel Deployment!

Your chatbot has been prepared for Vercel with the following changes:

### ✅ What I've Added:
- `vercel.json` - Vercel configuration
- `api/index.py` - Serverless function version of your chatbot
- Simplified keyword-based intent matching (faster for serverless)

### 📁 New Project Structure:
```
Chatbot/
├── api/
│   └── index.py          # Serverless Flask app
├── chatbot_server.py     # Original local development version
├── chatbot.py           # CLI version
├── chatbot.html         # Web interface
├── intents.json         # Training data
├── requirements.txt     # Dependencies
├── vercel.json          # Vercel config
└── README.md            # Documentation
```

### 🔧 Deployment Steps:

1. **Install Vercel CLI:**
   ```bash
   npm install -g vercel
   ```

2. **Deploy from your project directory:**
   ```bash
   cd C:\Users\akil2\OneDrive\Desktop\chat\Chatbot
   vercel
   ```

3. **Follow the prompts:**
   - Link to existing project or create new
   - Select Python runtime
   - Deploy!

### ⚠️ Important Notes:

- **Simplified AI**: Used keyword matching instead of ML for faster serverless performance
- **Cold Starts**: First request may be slower
- **Static Files**: HTML/CSS served directly by Vercel
- **Original Version**: Keep `chatbot_server.py` for local development with full ML

### 🔄 Alternative: Keep Full ML Version

If you want the full NLTK+scikit-learn version on Vercel:
- Expect slower cold starts (3-10 seconds)
- Higher memory usage
- NLTK downloads on first run

Let me know if you want to deploy the full ML version instead!
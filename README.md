# Chatbot

Small Python chatbot using Flask and a Naive Bayes classifier built from `intents.json`.

Quick start (Windows PowerShell):

1. Create and activate a virtual environment:

```powershell
python -m venv .venv; .\.venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

3. Run the server:

```powershell
python chatbot_server.py
```

4. Open a browser at http://127.0.0.1:5000

Notes:
- The first run of the server will download NLTK data (`punkt`, `wordnet`).
- If PowerShell prevents activating scripts, run: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser` (requires admin or current-user consent).

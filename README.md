# 🧠 A Council of Personalities

A Streamlit web app that answers a question by consulting multiple personality based agents and then synthesizing their perspectives into a single clear response.

Think of it as asking the same question to different ways of thinking and getting one balanced answer at the end.

---

## ✨ What this project does

- Lets you select different personality types (Analysts, Diplomats, Sentinels, Explorers)
- Sends the same question to all selected personalities
- Each personality responds from its own perspective
- A neutral agent combines all responses into one final answer
- Stores past questions and answers as memory (optional module)

---
## 🆕 New in v2 (Major updates)

This version significantly extends the original v1 app by adding user awareness, persistent memory, and semantic retrieval.

### 🔐 User authentication (MongoDB)

- Users can sign up and log in with a username and password
- Credentials are stored securely in MongoDB
- Passwords are hashed (no plaintext storage)
- Login state is managed using Streamlit session state
- Logout clears the session and resets the app

Each user is treated as an isolated identity across sessions.

---

### 🧠 Per user semantic memory (FAISS)

- The app now maintains **separate memory per user**
- Memory is stored as short, meaningful notes instead of raw conversations
- Each note is embedded into a vector space using sentence transformers
- FAISS is used for fast semantic similarity search
- Memory is persisted locally on disk and survives app restarts

This allows the system to recall relevant past knowledge based on meaning, not keywords.

---

### 📌 How memory works

1. The final synthesized answer is broken into short informational notes  
2. Each note is converted into a vector embedding  
3. Notes are stored in a FAISS index under the logged in user  
4. When a new question is asked:
   - Similar past notes are retrieved using vector similarity
   - Relevant memory is injected into the neutral agent’s synthesis step  

Memory is user specific and never shared across accounts.

---

### 🧱 Architectural improvements

- Clear separation of concerns:
  - `app.py` handles UI and session state
  - `auth.py` handles authentication logic
  - `db.py` handles MongoDB connections
  - `memory.py` handles FAISS based vector memory
  - `main.py` remains pure orchestration logic
- No Streamlit session state is accessed outside `app.py`
- No API keys or credentials are written to disk

---

### ⚠️ Notes and limitations

- Designed for local or small scale deployments
- Memory storage is file based (FAISS + pickle)
- No OAuth or external identity provider yet
- No parallel agent execution (still sequential)

---

### 🔮 Planned improvements

- Memory injection per agent (not just neutral)
- Memory decay and recency weighting
- Memory deduplication
- Memory inspection and management UI
- Optional vector DB backends (Chroma / Qdrant)
- OAuth based login (Google / GitHub)

---

## 🧠 Personality groups

### Analysts
Logical, strategic, idea focused  
INTP, ENTP, INTJ, ENTJ  

### Diplomats
Value driven, empathetic, people focused  
INFJ, ENFJ, INFP, ENFP  

### Sentinels
Practical, structured, reliable  
ESTJ, ISTJ, ISFJ, ESFJ  

### Explorers
Action oriented, adaptable, hands on  
ISTP, ESTP, ISFP, ESFP  

---

## 🚀 Getting started

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>
```
## 2. Create and activate a virtual environment

### Windows
```bash
python -m venv venv
venv\Scripts\activate
```

### MacOS/Linux
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the app
```bash
streamlit run app.py
```
The app will open in your browser automatically.
















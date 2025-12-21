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

## 🏗️ How it works (high level)

1. User enters an OpenAI API key in the sidebar  
2. User selects one or more personalities  
3. User asks a question  
4. Each selected personality agent generates a response  
5. A neutral agent synthesizes the responses  
6. Final answer is shown, along with individual perspectives  

All agents run using CrewAI with a sequential workflow.

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
















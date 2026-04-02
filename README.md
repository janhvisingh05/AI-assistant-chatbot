# 🤖 AI Assistant (RAG + Memory + Guardrails)

An intelligent AI-powered assistant built using **Retrieval-Augmented Generation (RAG)** with **chat memory** and **guardrails for safety and reliability**.

This system retrieves relevant context from documents, maintains conversation history, and ensures safe, high-quality responses using validation layers.

---

## 🚀 Features

### 🔍 Retrieval-Augmented Generation (RAG)
- Fetches relevant document chunks using embeddings
- Provides context-aware answers instead of generic LLM responses

### 🧠 Conversational Memory
- Stores chat history per user
- Maintains context across multiple queries

### 🛡️ Guardrails (Core Feature)
Ensures reliability at every stage:

- **Input Guard**
  - Blocks unsafe or invalid queries
- **Context Guard**
  - Ensures retrieved data is meaningful
- **Output Guard**
  - Filters weak or unsafe responses

### 📊 Logging & Debugging
- Full pipeline logging in terminal
- Tracks:
  - User input
  - Retrieved context
  - LLM output
  - Guardrail decisions

### 🌐 Streamlit UI
- Simple interactive interface
- Displays responses and chat history

---


### 🏗️ Project Structure

ai_assistant_project/
│
├── app.py # Main Streamlit app
│
├── database/
│ └── db.py # User + chat storage (SQLite)
│
├── rag/
│ └── retriever.py # Context retrieval (embeddings + similarity)
│
├── llm/
│ └── gemini.py # LLM response generation (Google Gemini)
│
├── guardrails/
│ ├── input_guard.py # Input validation
│ ├── context_guard.py # Context validation
│ └── output_guard.py # Output validation
│
├── utils/
│ └── memory.py # Chat history formatting
│
└── requirements.txt


---

---

## ⚙️ Installation

### 1. Clone the repository
```bash
git clone https://github.com/your-username/ai-assistant.git
cd ai-assistant



User Input
   ↓
Input Guard (validation)
   ↓
Retriever (RAG)
   ↓
Context Guard (relevance check)
   ↓
LLM (Gemini)
   ↓
Output Guard (quality/safety)
   ↓
Database (memory storage)
   ↓
Response to UI


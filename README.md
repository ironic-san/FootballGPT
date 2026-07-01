# ⚽ FootballGPT

FootballGPT is an AI-powered football assistant built using **Google Gemini**, **Retrieval-Augmented Generation (RAG)**, and **Streamlit**.

It combines the reasoning ability of Gemini with a football knowledge base created from official football documents, allowing users to ask questions about football rules, competitions, tactics, history, clubs, players, and more.

---

## 🚀 Live Demo

🌐 **Streamlit App:**  
https://footballgpt-bgwjmmkxlmvqqnfgqos3yq.streamlit.app/

---

# ✨ Features

- 🤖 Gemini AI powered responses
- 📚 Retrieval-Augmented Generation (RAG)
- ⚽ Official football knowledge base
- 🧠 Conversation memory
- 🔄 Automatic AI model fallback
- 📖 Source citations
- 🌍 FIFA World Cup knowledge
- 🏆 UEFA Champions League regulations
- 📜 IFAB Laws of the Game
- 🎯 Football tactics & strategy
- 💬 Modern Streamlit chat interface

---

# 🧠 Knowledge Base

FootballGPT retrieves information from multiple football documents including:

- 📘 IFAB Laws of the Game
- 🌍 FIFA World Cup History
- 📜 FIFA World Cup Regulations
- 📖 FIFA World Cup Anecdotes
- 🏆 UEFA Champions League Regulations
- 🎯 Football Intelligence & Tactics

---

# 🛠 Tech Stack

## Frontend

- Streamlit

## AI

- Google Gemini API

## Retrieval (RAG)

- LangChain
- ChromaDB
- Sentence Transformers
- HuggingFace Embeddings

## Programming Language

- Python

---

# 📂 Project Structure

```text
FootballGPT/

│
├── data/                     # Football PDF documents
├── vector_db/                # Chroma Vector Database
│
├── chatbot.py
├── rag.py
├── model_manager.py
├── prompts.py
├── config.py
├── streamlit_app.py
│
├── requirements.txt
├── environment_local.yml
├── README.md
└── .gitignore
```

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/FootballGPT.git
```

Move into the project

```bash
cd FootballGPT
```

Create a virtual environment (optional)

```bash
conda env create -f environment_local.yml
conda activate footballgpt
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 API Key

Create a `.env` file in the project root.

```env
GOOGLE_API_KEY=YOUR_API_KEY
```

Or when deploying to Streamlit Cloud, add:

```
GOOGLE_API_KEY=YOUR_API_KEY
```

inside **Secrets**.

---

# ▶️ Run Locally

```bash
streamlit run streamlit_app.py
```

---

# 📸 Screenshots

*(Add screenshots of the application here)*

---

# 🔄 Current Version

**FootballGPT v3.0**

### Implemented

- ✅ Multi-model AI
- ✅ Automatic model switching
- ✅ Conversation memory
- ✅ Retrieval-Augmented Generation (RAG)
- ✅ Multi-document knowledge base
- ✅ Chroma Vector Database
- ✅ Local HuggingFace embeddings
- ✅ Source citations
- ✅ Streamlit deployment

---

# 🔮 Future Improvements

- Live football API integration
- Match schedules
- Live scores
- League standings
- Player statistics
- Transfer news
- Hybrid Search (BM25 + Vector Search)
- Multi-modal support (images & tactics boards)

---

# 👨‍💻 Author

**Sanjeev Prasad**

Computer Science Engineering Student

Interested in:
- Artificial Intelligence
- Machine Learning
- Space Technology
- Geospatial AI

GitHub:
https://github.com/YOUR_USERNAME

LinkedIn:
https://linkedin.com/in/YOUR_LINKEDIN

---

# 📄 License

This project is intended for educational and portfolio purposes.
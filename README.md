# Obsidian-Vault-RAG-Knowledge-Assistant

# 📚 Obsidian Vault RAG Knowledge Assistant

An intelligent **Retrieval-Augmented Generation (RAG)** assistant that interacts with your Markdown notes. 
It doesn't just answer questions—it actively **creates and saves new structured notes** back into your vault, acting like an **AI Knowledge Manager**.

---

## ✨ Features

- **📂 Automated Vault Loading:** Reads and processes all `.md` files from your local `obsidian_notes` folder.
- **🧠 Semantic Search:** Uses Hugging Face embeddings and FAISS to find the most relevant context for your query.
- **🤖 AI-Powered Answers:** Generates contextual, accurate answers using **Google Gemini**.
- **💾 Note Creation (Agentic Twist):** After answering, it can generate a detailed summary and **save it as a new `.md` file** directly into your vault.
- **⚡ Lightning Fast:** Uses `st.cache_resource` for instant, repeatable vector-store loading.

---

## 🛠️ Tech Stack

| Category | Technology |
| :--- | :--- |
| **AI / LLM** | Google Gemini (`gemini-1.5-flash`) |
| **Retrieval** | LangChain + FAISS |
| **Embeddings** | Hugging Face (`all-MiniLM-L6-v2`) |
| **Frontend** | Streamlit |
| **Data Storage** | Local Markdown (`.md`) Files |

---

## 📁 Project Structure

```text
Obsidian_RAG_Assistant/
├── obsidian_notes/          # Contains your .md files (The "Vault")
│   ├── ai_basics.md
│   ├── react_js.md
│   └── ...
├── app.py                   # Main Streamlit application
├── requirements.txt         # Python dependencies
├── .env                     # Google API Key (DO NOT push to GitHub)
└── README.md                # Project documentation

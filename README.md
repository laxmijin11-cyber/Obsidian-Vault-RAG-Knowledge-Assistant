<p align="center">
  <img src="https://github.com/user-attachments/assets/f5f75640-227c-41f1-8216-e8e3418557a8" alt="Obsidian RAG Assistant Banner" width="100%"/>
</p>

<h1 align="center">📚 Obsidian Vault RAG Knowledge Assistant</h1>

<p align="center">
  <b>An intelligent AI Knowledge Manager that reads, retrieves, and writes your Markdown notes.</b>
</p>

<p align="center">
  <i>Powered by Google Gemini | LangChain | FAISS | Streamlit</i>
</p>

---

## ✨ Features

| Feature | Description |
| :--- | :--- |
| 📂 **Automated Vault Loading** | Seamlessly reads all `.md` files from your `obsidian_notes` folder. |
| 🧠 **Semantic Search** | Uses Hugging Face embeddings and FAISS to find the exact context for your query. |
| 🤖 **AI-Powered Answers** | Generates contextual, accurate answers using **Google Gemini**. |
| 💾 **Agentic Note Creation** | One-click button to generate a structured summary and save it as a new `.md` file. |
| ⚡ **Lightning Fast** | Uses `st.cache_resource` for instant, repeatable vector-store loading. |

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
Obsidian-Vault-RAG-Knowledge-Assistant/
├── obsidian_notes/          # Contains your .md files (The "Vault")
│   ├── ai_basics.md
│   ├── react_js.md
│   └── ...
├── app.py                   # Main Streamlit application
├── requirements.txt         # Python dependencies
├── .env                     # Google API Key (DO NOT push to GitHub)
└── README.md                # Project documentation
```
🚀 How to Run
1. Prerequisites

Python 3.10+

A free Google Gemini API Key (from aistudio.google.com)

2. Setup & Installation
bash
# 1. Clone the repository

git clone https://github.com/laxmijin11-cyber/Obsidian-Vault-RAG-Knowledge-Assistant.git

cd Obsidian-Vault-RAG-Knowledge-Assistant

# 2. Create and activate a virtual environment

python -m venv venv

.\venv\Scripts\activate  # On Windows

source venv/bin/activate # On Mac/Linux

# 3. Install dependencies

pip install -r requirements.txt

# 4. Configure API Key

# Create a .env file in the root directory and add:

# GOOGLE_API_KEY=your_key_here

3. Run the Application

bash

python -m streamlit run app.py


<img width="1881" height="850" alt="image" src="https://github.com/user-attachments/assets/7be64b56-543e-43c0-b3c2-c23c06980ff2" />


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

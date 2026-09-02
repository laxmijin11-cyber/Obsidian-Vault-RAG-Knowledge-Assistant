#  Obsidian Vault RAG Knowledge Assistant

<img width="924" height="609" alt="image" src="https://github.com/user-attachments/assets/f5f75640-227c-41f1-8216-e8e3418557a8" />


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

```
🚀 How to Run
1. Prerequisites
Python 3.10+

A Google Gemini API Key (Free)

2. Setup
bash
# 1. Clone the repository
git clone https://github.com/YOUR_USERNAME/Obsidian_RAG_Assistant.git
cd Obsidian_RAG_Assistant

# 2. Create and activate a virtual environment
python -m venv venv
.\venv\Scripts\activate  # On Windows
source venv/bin/activate # On Mac/Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Configure API Key
# Create a .env file in the root directory:
# GOOGLE_API_KEY=your_key_here

3. Run the Application
bash
python -m streamlit run app.py


How It Works
Ingestion: The load_vault() function reads all Markdown files in obsidian_notes.

Chunking & Embedding: Text is split into manageable chunks and converted into vectors using Hugging Face.

Vector Store: Chunks are stored in a FAISS database for fast semantic retrieval.

Query: When you ask a question, the assistant retrieves the most relevant chunks.

Generation: Google Gemini uses the retrieved context to answer accurately.

Agentic Action: The "Save Summary" button triggers the AI to create a new .md file, expanding your knowledge base automatically.


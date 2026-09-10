import streamlit as st
import os

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings

st.set_page_config(page_title="VaultIQ", page_icon="🧠", layout="wide")

# ---------- CUSTOM CSS ----------
st.markdown(
    """
<style>
    .stApp { background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%); }
    h1 {
        background: linear-gradient(90deg, #a78bfa 0%, #60a5fa 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800 !important;
        font-size: 2.8rem !important;
    }
    section[data-testid="stSidebar"] {
        background: rgba(15, 23, 42, 0.9);
        border-right: 1px solid rgba(255, 255, 255, 0.1);
    }
    .stTextInput input {
        background-color: #1e293b !important;
        color: #f1f5f9 !important;
        border: 1px solid #334155 !important;
        border-radius: 10px !important;
    }
    .stButton button {
        background: linear-gradient(90deg, #a78bfa 0%, #60a5fa 100%);
        color: white !important;
        border: none;
        border-radius: 10px;
        font-weight: 600;
        padding: 0.6rem 1.5rem;
    }
    .chat-user {
        background: linear-gradient(90deg, #a78bfa 0%, #8b5cf6 100%);
        color: white;
        padding: 1rem 1.5rem;
        border-radius: 15px 15px 15px 5px;
        margin: 0.5rem 0;
        max-width: 80%;
    }
    .chat-bot {
        background: rgba(51, 65, 85, 0.7);
        color: #f1f5f9;
        padding: 1rem 1.5rem;
        border-radius: 15px 15px 5px 15px;
        margin: 0.5rem 0;
        max-width: 85%;
        border-left: 3px solid #60a5fa;
    }
    .chat-label {
        font-size: 0.75rem;
        font-weight: 700;
        opacity: 0.7;
        margin-bottom: 0.3rem;
        letter-spacing: 1px;
    }
</style>
""",
    unsafe_allow_html=True,
)

st.title("🧠 VaultIQ")
st.caption(
    "✨ AI-powered assistant that reads, answers, and writes to your Obsidian vault."
)

# ---------- SIDEBAR ----------
with st.sidebar:
    st.markdown("## 🔑 Configuration")
    user_api_key = st.text_input(
        "Google Gemini API Key",
        type="password",
        placeholder="AIza...",
        help="Get a free key at https://aistudio.google.com/",
    )
    st.markdown("[🔗 Get your free Gemini API key →](https://aistudio.google.com/)")
    st.divider()
    st.markdown("### 📖 About")
    st.markdown("""
    **VaultIQ** uses **RAG** to search your notes and **autonomously writes** new summaries back into your vault.
    """)


# ---------- HELPER: Extract text from response ----------
def extract_text(response):
    content = response.content
    if isinstance(content, list):
        for block in content:
            if isinstance(block, dict) and block.get("type") == "text":
                return block.get("text", "")
        return str(content)
    return content


# ---------- LOAD VAULT ----------
def load_vault():
    text = ""
    if not os.path.exists("obsidian_notes"):
        return ""
    for filename in os.listdir("obsidian_notes"):
        if filename.endswith(".md"):
            with open(f"obsidian_notes/{filename}", "r", encoding="utf-8") as f:
                text += f.read() + "\n\n"
    return text


@st.cache_resource
def get_vector_store():
    text = load_vault()
    if not text.strip():
        return None
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = splitter.split_text(text)
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    return FAISS.from_texts(chunks, embedding=embeddings)


vector_store = get_vector_store()
if vector_store is None:
    st.error("⚠️ No notes found in `obsidian_notes/` folder.")
    st.stop()

if not user_api_key:
    st.info("👈 **Enter your Google Gemini API key in the sidebar to begin.**")
    st.stop()

llm = ChatGoogleGenerativeAI(
    model="models/gemini-3.5-flash",
    temperature=0.3,
    google_api_key=user_api_key,
)

# ---------- MAIN INTERFACE ----------
query = st.text_input("💬 Ask VaultIQ:", placeholder="e.g., What is React?")

if query:
    with st.spinner("🔍 Searching your knowledge base..."):
        docs = vector_store.similarity_search(query)
        context = "\n\n".join([doc.page_content for doc in docs])
        prompt = f"""Use the following context to answer the question.
        Context:
        {context}
        
        Question: {query}"""

        try:
            response = llm.invoke([HumanMessage(content=prompt)])
            answer_text = extract_text(response)

            st.markdown(
                f"""
            <div class="chat-user">
                <div class="chat-label">YOU</div>
                {query}
            </div>
            <div class="chat-bot">
                <div class="chat-label">VAULTIQ</div>
                {answer_text}
            </div>
            """,
                unsafe_allow_html=True,
            )

            if st.button("💾 Save as Note"):
                summary_prompt = f"Create a detailed markdown note summarizing: {query}\n\nContext: {context}"
                summary = llm.invoke([HumanMessage(content=summary_prompt)])
                summary_text = extract_text(summary)

                safe_filename = "".join(
                    [c for c in query if c.isalnum() or c == " "]
                ).replace(" ", "_")[:30]

                with open(
                    f"obsidian_notes/{safe_filename}.md", "w", encoding="utf-8"
                ) as f:
                    f.write(summary_text)
                st.success(f"✅ Saved `{safe_filename}.md` to your vault!")
        except Exception as e:
            st.error(f"⚠️ Error: {e}. Please check your API key.")

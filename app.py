import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings

st.set_page_config(page_title="Obsidian RAG Assistant", page_icon="📚")
st.title("📚 Obsidian Vault RAG Assistant")
st.caption("Ask questions about your notes, and it saves summaries back to your vault!")

llm = ChatGoogleGenerativeAI(model="models/gemini-1.5-flash", temperature=0.3)


def load_vault():
    text = ""
    for filename in os.listdir("obsidian_notes"):
        if filename.endswith(".md"):
            with open(f"obsidian_notes/{filename}", "r", encoding="utf-8") as f:
                text += f.read() + "\n\n"
    return text


@st.cache_resource
def get_vector_store():
    text = load_vault()
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = splitter.split_text(text)

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vector_store = FAISS.from_texts(chunks, embedding=embeddings)
    return vector_store


vector_store = get_vector_store()

query = st.text_input("Ask your Obsidian Vault:")
if query:
    docs = vector_store.similarity_search(query)
    context = "\n\n".join([doc.page_content for doc in docs])

    prompt = f"""
    Use the following context to answer the question.
    Context:
    {context}
    
    Question: {query}
    """
    response = llm.invoke([HumanMessage(content=prompt)])
    st.write(response.content)

    if st.button("💾 Save Summary as New Note"):
        summary_prompt = f"Create a detailed markdown note summarizing the following: {query}\n\nContext: {context}"
        summary = llm.invoke([HumanMessage(content=summary_prompt)])

        safe_filename = "".join([c for c in query if c.isalnum() or c == " "]).replace(
            " ", "_"
        )[:30]

        with open(f"obsidian_notes/{safe_filename}.md", "w", encoding="utf-8") as f:
            f.write(summary.content)

        st.success(f"Saved as {safe_filename}.md! (Check your vault)")

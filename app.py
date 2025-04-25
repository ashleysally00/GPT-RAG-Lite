import streamlit as st
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_openai import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain.schema import Document
import os

# Set OpenAI API Key
openai_api_key = os.getenv("OPENAI_API_KEY")

# Sample document
docs = [Document(page_content="Machine learning involves algorithms and data.")]
embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vectorstore = FAISS.from_documents(docs, embedding_model)
llm = ChatOpenAI(model_name="gpt-3.5-turbo", openai_api_key=openai_api_key)
qa_chain = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=vectorstore.as_retriever())

# Streamlit UI
st.title("GPT-RAG-Lite")
st.write("Ask a question based on the document:")

query = st.text_input("Enter your question:")
if query:
    response = qa_chain.run(query)
    st.write("### Response:")
    st.write(response)

from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_openai import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain.schema import Document
import os

# Manually define documents
docs = [Document(page_content="Machine learning involves algorithms and data.")]

# Embed documents
embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vectorstore = FAISS.from_documents(docs, embedding_model)

# Load LLM using OpenAI GPT-3.5
gpt_api_key = os.getenv("OPENAI_API_KEY")  # Make sure to set this environment variable
llm = ChatOpenAI(model_name="gpt-3.5-turbo", openai_api_key=gpt_api_key)

# Set up Retrieval QA
qa_chain = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=vectorstore.as_retriever())

# Example query
query = "What are the key principles of machine learning?"
response = qa_chain.run(query)
print("Query:", query)
print("Response:", response)

# GPT-RAG-Lite

**GPT-RAG-Lite** is a minimal and efficient Retrieval-Augmented Generation (RAG) system built with **LangChain**. It uses FAISS for vector search and OpenAI GPT-3.5 for natural language generation.

[![Streamlit App](https://img.shields.io/badge/Streamlit-Live_App-brightgreen?logo=streamlit)](https://mr7yntpqnzgoy2bgegwqop.streamlit.app)

🚀 **Test it live here**: [GPT-RAG-Lite Streamlit App](https://mr7yntpqnzgoy2bgegwqop.streamlit.app)


## Features
- 🔍 **Vector Search** powered by FAISS (in-memory, fast).
- 💬 **OpenAI GPT-3.5** for generating context-aware responses.
- 📝 Simple **manual or dynamic document** input.
- ⚡ Lightweight and easy to set up.

---

## Setup Instructions

1. **Clone the Repo**:
   ```bash
   git clone https://github.com/your-username/GPT-RAG-Lite.git
   cd GPT-RAG-Lite

2. **Set up the Virtual Environment**:

```
python -m venv venv
source venv/bin/activate
```

3. **Install Dependencies**:

```
pip install -r requirements.txt
```

4. **Set Your OpenAI API Key**:

```
export OPENAI_API_KEY=your_openai_api_key
```

5. **Run the App**:

   ```
   python rag-solution.py
   ```

**Example Output**

Query: What are the key principles of machine learning? <br>
Response: Key principles include data collection, preprocessing, model training, evaluation, and deployment.

## Streamlit Interface
![Streamlit Interface Screenshot](https://github.com/ashleysally00/GPT-RAG-Lite/blob/main/streamlit.png)

# Live Demo

Try the live app here: [GPT-RAG-Lite Streamlit App](https://mr7yntpqnzgoy2bgegwqop.streamlit.app)

---

## How to Deploy Your Own Streamlit App on Community Cloud

1. **Push your project to GitHub** as a public repository.
2. **Sign in to Streamlit Cloud** at [https://streamlit.io/cloud](https://streamlit.io/cloud) using GitHub.
3. **Create a New App**:
   - Click **"New app"**.
   - Select your GitHub repo.
   - Set the branch (e.g., `main`) and app file name (e.g., `app.py`).
   - Click **Deploy**.
4. **Set Secrets**:
   - Go to **Manage App → Secrets**.
   - Add your OpenAI key like this:
     ```toml
     OPENAI_API_KEY = "your_openai_api_key"
     ```
   - Save and redeploy if needed.

Your app will now be live and shareable with anyone via your Streamlit Cloud URL☁️☁️💖

---

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).


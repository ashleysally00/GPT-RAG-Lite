# GPT-RAG-Lite

**GPT-RAG-Lite** is a minimal and efficient Retrieval-Augmented Generation (RAG) system using FAISS for vector search and OpenAI GPT-3.5 for natural language generation.

---

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

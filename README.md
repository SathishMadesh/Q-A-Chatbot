# 🚀 LLM Q&A Web App (Streamlit + LangChain + Groq)

This project is a simple **LLM-powered Question & Answer web application** built using **Streamlit**, **LangChain**, and **Groq API**. It allows users to interact with different Large Language Models and dynamically control response behavior.

---

## 📌 Features

- ✅ Interactive UI using Streamlit  
- ✅ Multiple LLM model selection  
- ✅ Adjustable response parameters:
  - Temperature  
  - Max Tokens  
- ✅ Prompt engineering using LangChain  
- ✅ Output parsing with `StrOutputParser`  
- ✅ LangSmith tracing for monitoring and debugging  

---

## 🛠️ Tech Stack

- Python  
- Streamlit  
- LangChain  
- Groq API  
- dotenv  
- LangSmith  

---

## 📂 Project Structure



---

## ⚙️ Setup Instructions


###1️⃣ Clone the Repository

```bash
git clone <your-repo-link>
cd <your-project-folder>

### 2️⃣ Create Virtual Environment
python -m venv venv

### Activate the environment

### 3️⃣ Install Dependencies
pip install -r requirements.txt

### 🔐 Environment Variables

Create a .env file in the root directory and add the following:

GROQ_API_KEY=your_groq_api_key_here
LANGCHAIN_API_KEY=your_langsmith_api_key_here
LANGSMITH_PROJECT=your_project_name

### ▶️ Running the Application
streamlit run app.py

💡 How It Works
User enters a query in the Streamlit interface
The query is formatted using ChatPromptTemplate

LangChain builds a pipeline:

Prompt → LLM (Groq) → Output Parser
The response is generated and displayed in the UI

🔄 LLM Pipeline
Prompt Template
LLM (ChatGroq)
Output Parser

This modular pipeline makes it easy to extend and scale the application.

📊 Future Improvements
🔹 Add Retrieval-Augmented Generation (RAG)
🔹 Integrate vector databases (Chroma / FAISS)
🔹 Maintain chat history
🔹 Deploy to cloud platforms (Streamlit Cloud / Hugging Face)

👨‍💻 Author

Sathish M
Aspiring AI Engineer | Exploring LLMs, GenAI, and Data Science

⭐ Acknowledgements
LangChain for LLM orchestration
Groq for fast inference APIs
Streamlit for rapid UI development

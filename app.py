import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate


import os
from dotenv import load_dotenv

load_dotenv()

# Groq api key
os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")

# LangSmith Tracking
os.environ['LANGCHAIN_API_KEY']=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGSMITH_TRACING"]="true"
os.environ["LANGSMITH_PROJECT"]=os.getenv("LANGSMITH_PROJECT")


# Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system","You are an helpful assistant. Please responce to the user queries"),
        ("user", "Question:{question}")
    ]
)


def generate_responce(question, api_key, llm, temprature, max_tokens):
    llm = ChatGroq(model=llm)
    output_parser = StrOutputParser()
    chain = prompt|llm|output_parser
    answer = chain.invoke({'question':question})
    return answer


# Title of the app
st.sidebar.title("Settings")
api_key = st.sidebar.text_input("Enter your GROQ API key", type="password")

# Drop down to select the Models
llm = st.sidebar.selectbox("Select an AI Model",["llama-3.1-8b-instant","llama-3.3-70b-versatile","openai/gpt-oss-120b"])

# Adjust response parameter
temprature = st.sidebar.slider("temprature", min_value=0.0, max_value=1.0, value=0.7)
max_tokens= st.sidebar.slider("Max Tokens", min_value=50, max_value=300, value=150)

# Main interface for user input
st.write("Go ahead and ask any question")
user_input = st.text_input("You:")

if user_input:
    response = generate_responce(user_input,api_key,llm,temprature, max_tokens)
    st.write(response)
else:
    st.write("Please provide the query")
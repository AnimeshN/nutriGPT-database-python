import os
import streamlit as st
import requests
from dotenv import load_dotenv

# Set the page title and icon
st.set_page_config(
    page_title="Nutrition Insights for India 🥦🇮🇳",
    page_icon="🍏",
)

# Sidebar content
with st.sidebar:
    st.markdown(
        "## How to Use\n"
        "Explore and gain insights into the nutrition status of India. Feel free to ask questions like:\n"
        "1. Provide an overview of the health conditions in India?\n"
        "2. Which states are performing well in addressing malnutrition?"
    )
    st.markdown("---")
    st.markdown("# About NutriGPT")
    st.markdown(
        "NutriGPT is an AI-powered application that connects to a real-time SQLite database and generates data embeddings. "
        "It utilizes Pathway’s [LLM App features](https://github.com/pathwaycom/llm-app) "
        "to build a real-time Large Language Model (LLM)-enabled data pipeline in Python, combining data from multiple sources."
    )
    st.markdown("[View the source code on Animesh's GitHub](https://github.com/AnimeshN/chatgpt-database-python-nutrition)")

# Load environment variables
load_dotenv()
api_host = os.environ.get("HOST", "0.0.0.0")
api_port = int(os.environ.get("PORT", 8080))

# Streamlit UI elements
st.title("NutriGPT: Unlocking Nutrition Insights for India")

question = st.text_input(
    "Ask a Question",
    placeholder="Compare NFHS4 and NFHS5 data regarding the diabetes situation in India?",
)

if question:
    url = f'http://{api_host}:{api_port}/'
    data = {"query": question}

    response = requests.post(url, json=data)

    if response.status_code == 200:
        st.write("### Answer")
        st.write(response.json())
    else:
        st.error(f"Failed to send data to the Pathway API. Status code: {response.status_code}")

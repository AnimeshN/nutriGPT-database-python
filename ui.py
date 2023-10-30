import os
import streamlit as st
import requests
from dotenv import load_dotenv


with st.sidebar:
    st.markdown(
        "## How to use\n"
        "Just ask ask questions related to nutrition status of India. Following are few examples\n"
        "1. Give overview of indian health condiation?\n"
        "2. Which states are performing well in malnutrition?"
    )
    st.markdown("---")
    st.markdown("# About")
    st.markdown(
        "AI app connects to SQLite database in realtime and create embeddings "
        "It uses Pathway’s [LLM App features](https://github.com/pathwaycom/llm-app) "
        "to build real-time LLM(Large Language Model)-enabled data pipeline in Python and join data from multiple input sources\n"

    )
    st.markdown("[View the source code on Animesh's GitHub](https://github.com/AnimeshN/chatgpt-database-python-nutrition)")


# Load environment variables
load_dotenv()
api_host = os.environ.get("HOST", "0.0.0.0")
api_port = int(os.environ.get("PORT", 8080))


# Streamlit UI elements
st.title("NutriGPT")

question = st.text_input(
    "Ask the question",
    placeholder="What data are looking for?"
)


if question:
    url = f'http://{api_host}:{api_port}/'
    data = {"query": question}

    response = requests.post(url, json=data)

    if response.status_code == 200:
        st.write("### Answer")
        st.write(response.json())
    else:
        st.error(f"Failed to send data to Pathway API. Status code: {response.status_code}")

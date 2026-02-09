# config.py
import streamlit as st

# Get API key from Streamlit secrets
OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]

MODEL = "gpt-4o"

USERS = {
    "admin": "admin123",
    "demo": "demo123",
    "user": "password"
}

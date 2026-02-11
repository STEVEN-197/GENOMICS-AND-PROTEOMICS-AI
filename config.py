# config.py
import os
import streamlit as st

# Get Gemini API key from Streamlit secrets or environment
try:
    GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]
except:
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "AIzaSyAfW4fmMD366Q-sAO_G2OzwAhXBx0Rcq14")

# Latest Gemini model (February 2026)
MODEL = "gemini-2.0-flash-exp"

USERS = {
    "admin": "admin123",
    "demo": "demo123",
    "user": "password"
}

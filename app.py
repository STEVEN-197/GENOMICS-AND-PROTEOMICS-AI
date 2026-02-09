import streamlit as st
import openai
from datetime import datetime
import os

# ====== ─── SET YOUR ▼ OPENAI API KEY HERE ─── ===== #
openai.api_key = "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"

# -------- Function to query GPT-5.2 (latest) -------- #
def ask_gpt(query: str) -> str:
    try:
        response = openai.ChatCompletion.create(
            model="gpt-5.2-chat-latest",
            messages=[
                {"role": "system", "content": "You are a precise genomics & proteomics analysis assistant."},
                {"role": "user", "content": query}
            ],
            max_tokens=500,
            temperature=0.7,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"⚠️ API Error: {str(e)}"

# -------------- Streamlit UI -------------- #
st.markdown(f"<style>{open('assets/custom.css').read()}</style>", unsafe_allow_html=True)
st.markdown(f"<script>{open('assets/custom.js').read()}</script>", unsafe_allow_html=True)

st.title("🧬 Genomics & Proteomics AI Platform")

st.write("""
Welcome! Ask a question about functional genomics or proteomics,
and get **accurate, deep analytical answers** from ChatGPT’s latest model (GPT‑5.2). :contentReference[oaicite:2]{index=2}
""")

# Input section
query = st.text_area("🔍 Enter your question:")

if st.button("Submit"):
    if query.strip() == "":
        st.error("❗ Please type a valid query first.")
    else:
        st.info("⏳ Getting results...")
        answer = ask_gpt(query)
        st.session_state.setdefault("history", []).append({
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "query": query,
            "answer": answer,
        })
        st.success("✅ Analysis complete!")

# Display last answer and history
if "history" in st.session_state and st.session_state["history"]:
    st.markdown("---")
    st.subheader("📜 Previous Results")

    for item in reversed(st.session_state["history"]):
        st.markdown(f"<div class='query-box'><b>{item['time']}</b><br><i>Q:</i> {item['query']}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='answer-box'><b>A:</b> {item['answer']}</div>", unsafe_allow_html=True)

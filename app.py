import openai
import streamlit as st
import os
from datetime import datetime

# Set your OpenAI API key
openai.api_key = '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'

# Function to get response from OpenAI GPT model
def get_chatgpt_response(query):
    try:
        response = openai.Completion.create(
            engine="gpt-3.5-turbo",
            prompt=query,
            max_tokens=300,
            temperature=0.7
        )
        result = response.choices[0].text.strip()
        return result
    except Exception as e:
        return f"Error occurred: {e}"

# Create a dictionary to store previous results
if 'previous_queries' not in st.session_state:
    st.session_state.previous_queries = []

# Main page layout
def main():
    st.title("Functional Genomics & Proteomics AI Platform")

    # Home Page with Introduction and Navigation
    if st.sidebar.button("Home"):
        st.markdown("""
            # Welcome to the AI-Powered Functional Genomics & Proteomics Platform
            This platform uses the latest **ChatGPT** AI technology to help you analyze complex genomics and proteomics data.
            You can ask questions, and ChatGPT will provide accurate and insightful responses based on the latest scientific knowledge.
        """)

    # Sidebar to navigate between different sections
    with st.sidebar:
        st.header("Navigation")
        option = st.radio("Choose an Option", ["Home", "Ask Question", "Previous Results"])

    # Ask Question page
    if option == "Ask Question":
        ask_question_page()

    # Display Previous Queries page
    elif option == "Previous Results":
        display_previous_queries()

# Page for asking questions
def ask_question_page():
    st.header("Ask Your Genomics/Proteomics Question")

    # User input field for query
    user_input = st.text_area("Enter your analysis query:")

    if st.button("Submit Query"):
        if user_input:
            st.write("Processing your query... Please wait.")
            response = get_chatgpt_response(user_input)
            st.write("ChatGPT Response:")
            st.write(response)

            # Save the query and response
            save_previous_query(user_input, response)
        else:
            st.error("Please enter a valid query.")

# Save the question and response in session state
def save_previous_query(query, response):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    st.session_state.previous_queries.append({"query": query, "response": response, "timestamp": timestamp})

# Display Previous Queries
def display_previous_queries():
    st.header("Previous Search Results")
    if len(st.session_state.previous_queries) > 0:
        for idx, query_data in enumerate(st.session_state.previous_queries):
            st.markdown(f"### {idx + 1}. Query ({query_data['timestamp']})")
            st.write(f"**Question:** {query_data['query']}")
            st.write(f"**Answer:** {query_data['response']}")
    else:
        st.write("No previous results found. Ask a question to get started!")

if __name__ == "__main__":
    main()

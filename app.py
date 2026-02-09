import openai
import streamlit as st

# Set your OpenAI API key here (replace with your key)
openai.api_key = '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'

# Streamlit interface
def main():
    st.title("Functional Genomics and Proteomics Analysis using AI")
    st.write("""
    This platform leverages AI (ChatGPT) to assist in the analysis of genomics and proteomics data.
    You can enter queries related to functional genomics and proteomics, and ChatGPT will process and analyze the results.
    """)

    # User input for genomic/proteomic analysis
    user_input = st.text_area("Enter your analysis query:")

    if st.button("Submit Query"):
        if user_input:
            st.write("Processing query...")
            response = get_chatgpt_response(user_input)
            st.write("ChatGPT Analysis Result:")
            st.write(response)
        else:
            st.error("Please enter a valid query.")

def get_chatgpt_response(query):
    try:
        # Using GPT-3.5 for querying (replace with other models if needed)
        response = openai.Completion.create(
            engine="gpt-3.5-turbo",
            prompt=query,
            max_tokens=150,
            temperature=0.7
        )
        result = response.choices[0].text.strip()
        return result
    except Exception as e:
        return f"Error occurred: {e}"

if __name__ == "__main__":
    main()

# Custom Styling (Add this to the app.py file inside the main function)
st.markdown("""
    <style>
        .stApp {
            background-color: #f0f0f5;
            font-family: Arial, sans-serif;
        }
        .css-1v3fvcr {
            padding-top: 10px;
        }
        .css-1r6m0ry {
            padding: 20px;
            background: #0057e7;
            color: white;
            border-radius: 10px;
        }
        .stTextInput textarea {
            border: 2px solid #0057e7;
            border-radius: 5px;
            padding: 10px;
        }
        .stButton button {
            background-color: #0057e7;
            color: white;
            border-radius: 5px;
            padding: 10px;
            font-size: 16px;
        }
        .stButton button:hover {
            background-color: #003db3;
        }
        .stText {
            color: #333;
        }
    </style>
""", unsafe_allow_html=True)

# Add JavaScript for interactivity (Example: Changing button text after clicking)
st.markdown("""
    <script>
        document.querySelector('button').addEventListener('click', function() {
            this.innerHTML = 'Processing...';
        });
    </script>
""", unsafe_allow_html=True)

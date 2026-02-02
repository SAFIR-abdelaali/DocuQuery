import streamlit as st
from src.data_handler import load_schema, format_schema_for_ai
from src.ai_engine import generate_sql

st.title("DocuQuery: AI-Powered SQL Query Generator")
st.header("This is the Demo of the V1 of my DocuQuery.")

with st.sidebar:
    st.header("Configuration")
    uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])
if uploaded_file:
    df = load_schema(uploaded_file)
    if df is not None:
        st.success("Schema loaded successfully!")
        with st.expander("View Uploaded Schema"):
            st.dataframe(df)
        st.markdown("---")
        st.markdown("### Step 2: Ask a Question")
        user_question = st.text_input("Example: Show me all users from Casablanca")
        if user_question:
            schema_context = format_schema_for_ai(df)
            with st.spinner("Generating SQL..."):
                generated_sql = generate_sql(user_question, schema_context)
            
            st.code(generated_sql, language="sql")
else:
    st.info("Please upload a CSV file in the sidebar to begin.")
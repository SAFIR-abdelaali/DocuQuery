import os
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEndpoint

load_dotenv()
model_name = "Qwen/Qwen2.5-Coder-7B-Instruct"
llm = HuggingFaceEndpoint(
    repo_id=model_name,
    max_new_tokens=150,
    temperature=0.1, 
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_KEY")
)
#this function will help us transform the normal human questions into sql queries using the Qwen opensource llm
def generate_sql(question, schema_context):
    prompt = f"Given the following database schema:\n{schema_context}\nGenerate an SQL query for the following question:\n{question}\nSQL Query:"
    sql_query = llm.invoke(prompt)
    return sql_query

import os
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.messages import HumanMessage, SystemMessage
load_dotenv()
#had to do some mdification to the endpoint because the standard tas was conversational and here we need text-generation
model_id = "Qwen/Qwen2.5-Coder-7B-Instruct"
llm = HuggingFaceEndpoint(
    repo_id=model_id,
    task="text-generation", 
    max_new_tokens=150,
    temperature=0.1, 
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_KEY")
)
chat_model = ChatHuggingFace(llm=llm)
def generate_sql(question, schema_context):
    messages = [
        SystemMessage(content=(
            "You are a world-class SQL expert. "
            "Use the provided database schema to write a valid, optimized SQL query. "
            "Respond ONLY with the SQL code, no explanations or markdown backticks."
        )),
        HumanMessage(content=(
            f"Database Schema:\n{schema_context}\n\n"
            f"Question: {question}\n\n"
            f"SQL Query:"
        ))
    ]
    response = chat_model.invoke(messages)
    return response.content.strip()
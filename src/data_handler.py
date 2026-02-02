import pandas as pd
import streamlit as st

def load_schema(uploaded_file):
    try:
        df = pd.read_csv(uploaded_file)
        required_cols = {'table_name', 'column_name','data_type'}
        if not required_cols.issubset(df.columns):
            st.error(f"Missing required columns: {required_cols - set(df.columns)}")
            return None
        return df
    except Exception as e:
        st.error(f"Error csv load: {e}")
        return None
    
def format_schema_for_ai(df):
    schema_text = ""
    for table in df['table_name'].unique():
        cols = df[df['table_name'] == table]
        col_string = ", ".join([f"{row['column_name']} ({row['data_type']})" for _, row in cols.iterrows()])
        schema_text += f"Table {table} has columns: {col_string}\n"
    return schema_text

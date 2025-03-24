import requests
import pandas as pd
from rag import IONetDataAgents
from qdrant_client import QdrantClient
import streamlit as st

IOINTELLIGENCE_API_KEY = st.secrets["brain"]["iointel_key"]

vn = IONetDataAgents(config={
     'client': QdrantClient(url=st.secrets["rag"]["qdrant_api"],
                                api_key=st.secrets["rag"]["qdrant_api_key"]),
     'model': 'meta-llama/Llama-3.3-70B-Instruct',
     'max_retries': 2,
     'api_key': IOINTELLIGENCE_API_KEY,
     'base_url': 'https://api.intelligence.io.solutions/api/v1'
    }
)

def query_clickhouse(sql):
    url = "https://crypto-clickhouse.clickhouse.com:8443/"
    params = {
        "user": "crypto",
        "password": ""
    }
    data = sql
    
    response = requests.post(url, params=params, data=data)
    
    if response.status_code == 200:
        return response.text
    else:
        raise Exception(f"Query failed with status {response.status_code}: {response.text}")
    

def add_ddl_rag():
    result = query_clickhouse("show tables from solana")
    tabl_explr = {}
    for tabl in result.split("\n")[:-1]:
        tabl_explr[tabl] = query_clickhouse(f"SHOW CREATE TABLE solana.{tabl}")
    # df_information_schema = pd.DataFrame(tabl_explr,index=range(len(tabl_explr)))
    # df = df_information_schema.T[0].reset_index()
    # df.columns = ["table_name","ddl"]
    # df["database"] ="default"
    # df["table_schema"] = "solana"
    # plan = vn.get_training_plan_generic(df)
    for tbl in tabl_explr:
        vn.add_ddl(ddl=tabl_explr[tbl])


def add_useful_queries_to_rag():
    solana_queries = query_clickhouse("select name,query from queries where group = 'Solana'")
    schema_query = solana_queries.split("\n")
    for s in schema_query:
        question,query = s.split("\t")
        print(question)
        vn.add_question_sql(question=question,sql=query)


if __name__ =='__main__':
    add_ddl_rag()
    add_useful_queries_to_rag()

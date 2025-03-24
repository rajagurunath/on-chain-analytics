import requests
import pandas as pd
import json

def query_clickhouse(sql):
    url = "https://crypto-clickhouse.clickhouse.com:8443/"
    params = {
        "user": "crypto",
        "password": ""
    }
    data = sql
    
    response = requests.post(url, params=params, data=data)
    
    if response.status_code == 200:
        res_json = json.loads(response.text)
        return pd.DataFrame(res_json['data'])
    else:
        raise Exception(f"Query failed with status {response.status_code}: {response.text}")
    
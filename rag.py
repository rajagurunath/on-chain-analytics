
from vanna.base import VannaBase
from vanna.qdrant import Qdrant_VectorStore
from qdrant_client import QdrantClient
from langchain_openai import ChatOpenAI
from langfuse.decorators import observe
from observability import get_langfuse_handler

class IOIntelligence(VannaBase):
  def __init__(self, config={}):
      
    self.llm = ChatOpenAI(
        model= config.get("model"),
        temperature=config.get("temperature"),
        # max_tokens=config.get("max_tokens"),
        timeout=config.get("timeout"),
        # max_retries=config.get("max_retries"),
        api_key=config.get("api_key"),
        base_url=config.get("base_url"),
    )
  def system_message(self, message: str) -> any:
        return {"role": "system", "content": message}

  def user_message(self, message: str) -> any:
        return {"role": "user", "content": message}

  def assistant_message(self, message: str) -> any:
        return {"role": "assistant", "content": message}

  def generate_sql(self, question: str, **kwargs) -> str:
        # Use the super generate_sql
        print("generate_sql:",question)
        question += """ Note: Very important: generate sql with fully qualified table_names i.e {schema_name}.{table_name} example block_rewards.blocks Always follow this one and also make sure to 
        add `FORMAT JSON` at the end of the query to get the results in json code
        Two important points:
         - fully qualified table name
         - Json output response 
        
        """
        sql = super().generate_sql(question, **kwargs)
        print(sql)
        # Replace "\_" with "_"
        sql = sql.replace("\\_", "_")

        return sql
  def __clickhouse_capacity_prompt(self):
       return """
       "Note: Important! make sure you generate query to scan and load as less data as possible (because clickhouse as some capacity quota assigned for this user) "
            for example if user asks for more than 15 days for large data go back to 10 days query.
      """
  
#   @observe()
  def submit_prompt(self, prompt, **kwargs) -> str:
      prompt += prompt + self.__clickhouse_capacity_prompt
      ai_msg = self.llm.invoke(prompt,config={"callbacks": [get_langfuse_handler()]})
      return ai_msg.content

#   def generate_query_explanation(self, sql: str):
#       my_prompt = [
#             self.system_message("""You are a helpful assistant which prepares json document with sqlexplanation and schema 
#                     - explain a SQL query
#                     - Also provide schema name separately in a json format 
#                     example {"explanation":"This sql queries blocks table and provides number of records", schema:"block_rewards"}
#                     Note: your job is to output a json, dont speak anything else
#                     """),
#             self.user_message("json: " + sql),
#         ]
#       return self.submit_prompt(prompt=my_prompt)
  def generate_query_explanation(self, sql: str):
        my_prompt = [
            self.system_message("You are a helpful assistant that will explain a SQL query covering their main points only (TLDR version)"),
            self.user_message("Explain this SQL query in two lines: " + sql),
        ]

        return self.submit_prompt(prompt=my_prompt)


class IONetDataAgents(Qdrant_VectorStore, IOIntelligence):
    def __init__(self, config={}):
        Qdrant_VectorStore.__init__(self, config=config)
        IOIntelligence.__init__(self, config=config)

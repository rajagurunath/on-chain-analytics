import streamlit as st
from rag import IONetDataAgents
from langfuse.decorators import observe
from qdrant_client import QdrantClient
from streamlit_extras.chart_container import chart_container
from train_layout import train_layout
from about_us import about_us_layout
from data_source import data_source_layout
from database import query_clickhouse
# Define CSS styles
css = """
<style>
.custom-container {
    border: 2px solid white;
    border-radius: 8px;
    padding: 10px;
    margin-bottom: 20px;
}
</style>
"""

# Inject CSS into the Streamlit app
st.markdown(css, unsafe_allow_html=True)
IOINTELLIGENCE_API_KEY = st.secrets["brain"]["iointel_key"]
# st.set_page_config(page_title="IONET Data Chat", layout="wide")




vn = IONetDataAgents(config={
     'client': QdrantClient(url=st.secrets["rag"]["qdrant_api"],
                                api_key=st.secrets["rag"]["qdrant_api_key"]),
     'model': 'meta-llama/Llama-3.3-70B-Instruct',
     'max_retries': 2,
     'api_key': IOINTELLIGENCE_API_KEY,
     'base_url': 'https://api.intelligence.io.solutions/api/v1'
    }
)
vn.run_sql = query_clickhouse
vn.run_sql_is_set = True

def get_text():
    input_text = st.text_input(
        "You: ", "", key="input", placeholder="Talk to your data"
    )
    return input_text

def generate_markdown_list(questions):
    """
    Takes a list of strings and returns a Markdown-formatted list.
    """
    markdown_list = "\n".join(f"- {q}" for q in questions)
    return markdown_list


# use cache carefully it may repeat the same error
@st.cache_data
def query(user_input):
    sql = vn.generate_sql(question=user_input)
    df = vn.run_sql(sql=sql)
    explain = vn.generate_query_explanation(sql=sql)
    viz_code = vn.generate_plotly_code(question=user_input,sql=sql,df_metadata=df)
    fig = vn.get_plotly_figure(plotly_code=viz_code, df=df)
    followup_questions = vn.generate_followup_questions(question=user_input,sql=sql,df=df,n_questions=5)
    return {"sql":sql,"df":df,"plotly_fig":fig,"followup_questions":followup_questions,"explain":explain}

def chat_layout(vn):
    
    user_input = get_text()
    if user_input and (user_input != ""):
        placeholder = st.empty()
        with placeholder:
            try:
                output = query(user_input)
                df = output["df"]
                sql = output["sql"]
                with placeholder.container():
                    col1, col2 = st.columns([2, 2])
                    with col1:
                        st.info("Generated SQL")
                        st.markdown('<div class="sql-container">', unsafe_allow_html=True)
                        st.code(sql, language="sql")
                        st.markdown('</div>', unsafe_allow_html=True)
                    with col2:
                        st.info("Explanation")
                        st.markdown('<div class="sql-container">', unsafe_allow_html=True)
                        st.text(output["explain"])
                        st.markdown('</div>', unsafe_allow_html=True)
                    
                    with chart_container(df):
                        st.plotly_chart(figure_or_data=output["plotly_fig"])
                    
                    st.subheader("Follow-up Questions")
                    st.markdown(generate_markdown_list(output["followup_questions"]))
                    
            except Exception as e:
                st.image("https://media.tenor.com/a7LPdLTShOsAAAAC/vadivelu.gif")
                st.warning(f"Its not you, its us... we have noted this error, will be working to fix this error soon : - {e}")



layout_dict = {"Talk to Data": chat_layout,
               "Blockchain Data Source":data_source_layout,
               "Training":train_layout,
               "About IO":about_us_layout}

def main_layout():
    col1, col2 = st.columns(2)
    col1.image("https://io.net/_next/static/media/brandLogoLeft.29930dac.svg")

    with st.sidebar:
        st.image("https://io.net/_next/static/media/brandLogoRight.fd489776.svg")
        selected_tab = st.radio("", list(layout_dict.keys()))
        st.write("---")
    st.header(selected_tab)
    layout_dict[selected_tab](vn)


main_layout()
    


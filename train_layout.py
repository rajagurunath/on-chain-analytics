import streamlit as st
import pandas as pd
from vanna.base import VannaBase
# Configure the page with dark theme
st.set_page_config(page_title="Training Data Management", layout="wide")

# # Apply dark theme styles
# st.markdown("""
#     <style>
#         .stApp {
#             background-color: #1E1E1E;
#             color: #FFFFFF;
#         }
#         .data-table {
#             background-color: #2D2D2D;
#             border: 1px solid #404040;
#             border-radius: 10px;
#             padding: 20px;
#         }
#         .stButton button {
#             background-color: #404040;
#             color: #FFFFFF;
#             border: none;
#             padding: 8px 16px;
#             border-radius: 5px;
#         }
#         .stButton button:hover {
#             background-color: #505050;
#         }
#         .stTextInput input {
#             background-color: #2D2D2D;
#             color: #FFFFFF;
#             border: 1px solid #404040;
#         }
#         .stTextArea textarea {
#             background-color: #2D2D2D;
#             color: #FFFFFF;
#             border: 1px solid #404040;
#         }
#     </style>
# """, unsafe_allow_html=True)

def train_layout(vn:VannaBase):
    st.title("🎓 Training Data Management")
    
    # Display existing question-SQL pairs
    col1, col2 = st.columns(2)
    col1.subheader("Check the Training Data")
    text_search = col2.text_input("use me to search the Traning Data")
    pairs = vn.get_similar_question_sql(text_search,limit=500)
    if pairs:
        df = pd.DataFrame(pairs)
        df.columns = ["Question", "SQL Query"]
        st.dataframe(df, use_container_width=True)
        st.info(f"Total training pairs: {len(pairs)}")
    else:
        st.warning("No training data available yet.")

    # Add new training pairs
    st.subheader("Add New Training Pair")
    with st.form("add_training_pair"):
        question = st.text_input("Question")
        sql = st.text_area("SQL Query")
        submitted = st.form_submit_button("Add Training Pair")
        
        if submitted and question and sql:
            try:
                vn.add_question_sql(question=question, sql=sql)
                st.success("Successfully added new training pair!")
                st.rerun()
            except Exception as e:
                st.error(f"Error adding training pair: {e}")

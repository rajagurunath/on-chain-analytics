from langfuse.callback import CallbackHandler
import streamlit as st


def get_langfuse_handler():
    langfuse_handler = CallbackHandler(
        secret_key=st.secrets["langfuse"]["secret_key"],
        public_key=st.secrets["langfuse"]["public_key"],
        host="https://cloud.langfuse.com"
        )
    return langfuse_handler
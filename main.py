import streamlit as st
from src.components.header import render_head
from src.components.store import configure_store

render_head()

configure_store()
    
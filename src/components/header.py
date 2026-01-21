import streamlit as st

def render_head():
    st.set_page_config(
        page_title="Options Strategy Builder",
        initial_sidebar_state="collapsed",
        page_icon="📈",
        menu_items={
            'Report a bug': "https://github.com/harryph1ll1ps/options_strategies/issues/new",
            'About': "# Build an options trading strategy",
        }
    )

    st.header('Build Options Trading Strategy')
import streamlit as st

def render_head():
    st.set_page_config(
        page_title="Options Strategy Builder",
        initial_sidebar_state="collapsed",
        page_icon="📈",
        menu_items={
            'Report a bug': "https://github.com/your-username/options_strategies/issues",
            'About': "# Build an options trading strategy",
        }
    )

    st.title("Build An Options Strategy")
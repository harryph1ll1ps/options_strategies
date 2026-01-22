import streamlit as st

def render_head():
    st.set_page_config(
        page_title="Options Strategy Builder",
        initial_sidebar_state="collapsed",
        page_icon="📈",
        menu_items={
            'Report a bug': "https://github.com/harryph1ll1ps/options_strategies/issues/new",
            'About': (
                "An interactive options strategy builder for analysing multi-leg option trades. "
                "Design call and put strategies, visualise payoff structures, "
                "and generate AI-powered summaries covering strategy type, risk, and market assumptions. "
                "Built for traders who want a clear, intuitive way to reason about options payoffs."
            ),        }
    )

    st.header('Build Options Trading Strategy')
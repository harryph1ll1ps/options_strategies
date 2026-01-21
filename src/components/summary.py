import streamlit as st
from src.utils.llm import call_gemini, call_openrouter
import time

def build_context():
    """ Build the trade context to pass into LLM"""
    
    context = ""
    trade_no = 0

    for leg in st.session_state.legs:
        trade_no += 1

        option_type = leg["option_type"]
        direction = leg["direction"]
        strike = leg["strike"]
        premium = leg["premium"]

        context = context + f"Trade {trade_no}: {direction} {option_type} trading at strike price of {strike}, with a premium of {premium}.\n"

    return context


def render_ai_summary():
    
    def _show_ai_summary():
        st.session_state.show_ai_summary = True

    def _hide_ai_summary():
        st.session_state.show_ai_summary = False
        st.session_state.previous_ai_summary = False

    def _refresh_ai_summary():
        st.session_state.refresh_ai_summary = True

    st.markdown('---')
    st.markdown('### AI Summary')

    if st.session_state.show_ai_summary:
        col1, col2 = st.columns([0.25,0.75])
        with col1:
            st.button("Close Summary", on_click=_hide_ai_summary, icon="❌", key="ai_summary_exit_button")
        with col2:
            st.button("Reload", on_click=_refresh_ai_summary, icon="🔄", key="ai_summary_refresh_button")

    else:
        st.button("Show Summary", on_click=_show_ai_summary, icon="🧠", key="summary_button")


    if st.session_state.show_ai_summary and ((not st.session_state.previous_ai_summary) or st.session_state.refresh_ai_summary):
        with st.spinner('Generating analysis...'):
            trade_context = build_context()
            context = f"""
            You are a professional options trader and risk analyst.
            Analyse the following option legs as a single, unified strategy, not as individual trades.

            Output requirements:
            Write in a professional but accessible tone, suitable for an informed retail or institutional trader
            Be concise, high-level, and conceptual rather than numerically precise
            Do not over-focus on exact strike prices or premiums; use them only to infer structure and payoff
            Avoid unnecessary jargon or edge-case details
            Structure your response exactly as follows (markdown, bold section headers):

            Strategy Name:
            Identify the commonly accepted strategy name (e.g. vertical spread, straddle, condor). If none clearly applies, write 'N/A'.

            Overview:
            One plain-English sentence explaining what the trade is trying to achieve and the market view it expresses.

            Economics:
            Explain how the trade makes money and how it loses money in general terms, including payoff shape and where gains or losses are capped.

            Risks:
            Describe the primary risks (e.g. directional risk, time decay, capped upside, volatility changes), focusing on what could go wrong.

            Assumptions:
            State the key assumptions required for the trade thesis to hold (e.g. price movement, volatility behaviour, liquidity, early exercise considerations).

            Option legs:
            List the option legs exactly as provided, without reinterpretation.

            Here are the option legs to analyse:
            {trade_context}
            """.strip()

            response = call_openrouter(context)
            st.session_state.previous_ai_summary = response
            st.session_state.refresh_ai_summary = False

            with st.expander("View Strategy Details", expanded=True):
                st.markdown(response)


    elif st.session_state.show_ai_summary and st.session_state.previous_ai_summary:
        with st.expander("View Strategy Details", expanded=True):
            st.markdown(st.session_state.previous_ai_summary)

import streamlit as st
from src.utils.llm import call_gemini, call_openrouter

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

    st.markdown('---')
    st.markdown('### More Tools')

    if not st.session_state.show_ai_summary:
        st.button("AI Summary", on_click=_show_ai_summary, icon="🧠", key="summary_button")

    if st.session_state.show_ai_summary:
        st.button("Close Summary", on_click=_hide_ai_summary, icon="❌", key="ai_summary_exit_button")

        trade_context = build_context()
        context = f"""
        You are an experienced options trader and risk analyst.

        Given the following option legs, analyse the overall strategy as a single trade.

        For your response:
        - Start with a 1-2 sentence plain-English summary of the trade
        - Identify the strategy name if applicable (e.g. spread, straddle, condor)
        - Describe the **maximum upside** and **maximum downside**
        - Explain how the trade makes money and how it loses money
        - Highlight key risks (e.g. directional risk, volatility risk, assignment risk)
        - Mention any important assumptions you are making
        - Be succinct, logical, and clear
        - Return the response as markdown

        Option legs:
        {trade_context}
        """.strip()

        response = call_openrouter(context)

        st.markdown(response)


        


import streamlit as st

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

    st.markdown('---')
    st.markdown('### More Tools')

    st.button("AI Summary", on_click=_show_ai_summary, icon="🧠", key="summary_button")
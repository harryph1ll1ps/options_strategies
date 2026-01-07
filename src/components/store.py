import streamlit as st

def configure_store():
    """ Set up the application state """

    # default to having a singular long call leg
    if 'legs' not in st.session_state:
        st.session_state.legs = [{'option_type': 'call', 
                                  'direction': 'long', 
                                  'strike': 500, 
                                  'premium': 1}]
        
    if 'asset_price' not in st.session_state:
        st.session_state.asset_price = 500.0
        
    # hide the payoff diagram section by default
    if 'show_payoff_diagram' not in st.session_state:
        st.session_state.show_payoff_diagram = False

    # hide the AI summary section by default
    if 'show_ai_summary' not in st.session_state:
        st.session_state.show_ai_summary = False
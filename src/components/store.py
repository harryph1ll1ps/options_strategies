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

    if 'min_spot_price' not in st.session_state:
        st.session_state.min_spot_price = 0

    if 'max_spot_price' not in st.session_state:
        st.session_state.max_spot_price = 1000

    # hide the AI summary section by default
    if 'show_ai_summary' not in st.session_state:
        st.session_state.show_ai_summary = False

    if 'previous_ai_summary' not in st.session_state:
        st.session_state.previous_ai_summary = False
    
    if 'refresh_ai_summary' not in st.session_state:
        st.session_state.refresh_ai_summary = False

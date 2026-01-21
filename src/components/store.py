import streamlit as st

BASE_STRIKE = 500
BASE_PREMIUM = 1
BASE_SPOT_CEIL = 1000
BASE_SPOT_FLOOR = 0

def configure_store():
    """ Set up the application state """

    # default to having a singular long call leg
    if 'legs' not in st.session_state:
        st.session_state.legs = [{'option_type': 'Call', 
                                  'direction': 'Long', 
                                  'strike': BASE_STRIKE, 
                                  'premium': BASE_PREMIUM}]
        

        
    # hide the payoff diagram section by default
    if 'show_payoff_diagram' not in st.session_state:
        st.session_state.show_payoff_diagram = False

    if 'min_spot_price' not in st.session_state:
        st.session_state.min_spot_price = BASE_SPOT_FLOOR

    if 'max_spot_price' not in st.session_state:
        st.session_state.max_spot_price = BASE_SPOT_CEIL

    if "prev_min_spot_price" not in st.session_state:
        st.session_state.prev_min_spot_price = None

    if "prev_max_spot_price" not in st.session_state:
        st.session_state.prev_max_spot_price = None

    if 'spot_price' not in st.session_state:
        st.session_state.spot_price = float((BASE_SPOT_FLOOR + BASE_SPOT_CEIL) / 2)

    # hide the AI summary section by default
    if 'show_ai_summary' not in st.session_state:
        st.session_state.show_ai_summary = False

    if 'previous_ai_summary' not in st.session_state:
        st.session_state.previous_ai_summary = False
    
    if 'refresh_ai_summary' not in st.session_state:
        st.session_state.refresh_ai_summary = False

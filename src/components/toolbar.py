import streamlit as st

MAX_TRADES = 5
MIN_TRADES = 1 

def _handle_add_leg():
    if len(st.session_state.legs) < MAX_TRADES:
        st.session_state.legs.append({'option_type': 'Call', 
                                    'direction': 'Long', 
                                    'strike': 500.0, 
                                    'premium': 1.0})
    else:
        st.warning(f"You can only have up to {MAX_TRADES} trades.")

def _handle_remove_leg():
    if len(st.session_state.legs) > MIN_TRADES:
        st.session_state.legs.pop()
    else:
        st.warning(f"You must have at least {MIN_TRADES} trade.")


def render_trade_toolbar():
    with st.container():
        col1, col2 = st.columns([0.6,0.4])

        with col1:
            st.button("Add Trade", on_click=_handle_add_leg, type="primary", key="add_trade_button")
        
        with col2:
            st.button("Remove Trade", on_click=_handle_remove_leg, key="remove_trade_button")
        

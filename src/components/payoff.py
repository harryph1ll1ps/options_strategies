import streamlit as st
from src.utils.math import calculate_legs_return

def render_payoff():
    payoff, net_payoff = calculate_legs_return(st.session_state.legs, st.session_state.asset_price)

    st.markdown(f'**At an underlying price of** `{st.session_state.asset_price}` **gross payoff is** `{payoff}`')
    st.markdown(f'**At an underlying price of** `{st.session_state.asset_price}` **net payoff is** `{net_payoff}`')

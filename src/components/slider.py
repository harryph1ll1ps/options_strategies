import streamlit as st
from src.utils.math import calculate_legs_return


def render_slider():

    st.markdown('---')
    st.markdown('### Payoff Structure')
    
    st.slider("Spot Price",
              min_value=0.0,
              max_value=1000.0,
              value=st.session_state.asset_price,
              step=0.5,
              key="asset_price",
              )

    # display gross + net payoff
    payoff, net_payoff = calculate_legs_return(st.session_state.legs, st.session_state.asset_price)

    st.markdown(f'**At an underlying price of** `{st.session_state.asset_price}` **gross payoff is** `{payoff}`')
    st.markdown(f'**At an underlying price of** `{st.session_state.asset_price}` **net payoff is** `{net_payoff}`')

import streamlit as st
from src.utils.calculation import calculate_legs_return


def _get_range():
    strikes = [leg["strike"] for leg in st.session_state["legs"]]

    if strikes:
        lower = min(strikes) * 0.9
        upper = max(strikes) * 1.1

        lower_rounded_500 = lower - (lower % 500)
        upper_rounded_500 = upper + (500 - (upper % 500))

        st.session_state.min_spot_price = lower_rounded_500
        st.session_state.max_spot_price = upper_rounded_500


def render_slider():

    st.markdown('---')
    st.markdown('### Payoff Structure')
    
    _get_range()

    st.slider("Spot Price",
              min_value=0.0,
              max_value=st.session_state.max_spot_price,
              step=0.5,
              key="spot_price",
              )

    # display gross + net payoff
    payoff, net_payoff = calculate_legs_return(st.session_state.legs, st.session_state.spot_price)

    st.markdown(f'**At a spot price of** `{st.session_state.spot_price}` ***gross payoff*** **at expiry is** `{payoff}`')
    st.markdown(f'**At a spot price of** `{st.session_state.spot_price}` ***net payoff*** **at expiry is** `{net_payoff}`')

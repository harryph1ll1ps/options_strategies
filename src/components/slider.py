import streamlit as st
from src.utils.calculation import calculate_legs_return


def _get_range():
    strikes = [leg["strike"] for leg in st.session_state["legs"]]

    if not strikes:
        return 
    
    # compute new bounds
    lower = min(strikes) * 0.9
    upper = max(strikes) * 1.1

    new_min = lower - (lower % 100)
    new_max = upper + (100 - (upper % 100))

    # store old bounds
    old_min = st.session_state.prev_min_spot_price
    old_max = st.session_state.prev_max_spot_price
    old_spot = st.session_state.spot_price

    # determine if the range has been altered
    range_altered = (
        old_min is not None
        and old_max is not None
        and (new_min != old_min or new_max != old_max))

    # update bounds
    st.session_state.min_spot_price = new_min
    st.session_state.max_spot_price = new_max

    # if the range has been altered get the same relative location of spot price
    if range_altered:
        old_range = old_max - old_min
        new_range = new_max - new_min

        if old_range > 0:
            ratio = (old_spot - old_min) / old_range
        else:
            ratio = 0.5 # handles case where old range = 0 (one leg)

        st.session_state.spot_price = round(new_min + ratio * new_range, 2)

    # store current range for next rerun
    st.session_state.prev_min_spot_price = new_min
    st.session_state.prev_max_spot_price = new_max



def render_slider():

    st.markdown('---')
    st.markdown('### Payoff Structure')
    
    _get_range()

    st.slider("Spot Price",
              min_value=st.session_state.min_spot_price,
              max_value=st.session_state.max_spot_price,
              step=0.5,
              key="spot_price",
              )

    # display gross + net payoff
    payoff, net_payoff = calculate_legs_return(st.session_state.legs, st.session_state.spot_price)

    st.markdown(f'**At a spot price of** `{st.session_state.spot_price:.1f}` ***gross payoff*** **at expiry is** `{payoff:.1f}`')
    st.markdown(f'**At a spot price of** `{st.session_state.spot_price:.1f}` ***net payoff*** **at expiry is** `{net_payoff:.1f}`')
    st.markdown("")
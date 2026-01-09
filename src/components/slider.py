import streamlit as st

def render_slider():
    st.markdown('---')
    st.markdown('### Select Underlying Asset Price')
    st.slider("Spot Price",
              min_value=0.0,
              max_value=1000.0,
              value=st.session_state.asset_price,
              step=0.5,
              key="asset_price",
              )

import streamlit as st

def render_legs():
    """ Render Option Leg Inputs """
    col1, col2, col3, col4 = st.columns(4)

    for i, leg in enumerate(st.session_state['legs']):
        with col1:
            st.session_state['legs'][i]['option_type'] = st.selectbox(
                f"Option Type {i+1}", 
                ["Call","Put"], 
                index = 0 if leg['option_type'] == "Call" else 1,
                key=f"option_type_{i}"
                )
            
        with col2:
            st.session_state['legs'][i]['direction'] = st.selectbox(
                "Direction", 
                ["Long","Short"], 
                index = 0 if leg['direction'] == "Call" else 1,
                key=f"option_direction_{i}"
                )

        with col3:
            st.session_state['legs'][i]['strike'] = st.number_input(
                "Strike Price", 
                value = leg["strike"],
                key=f"strike_{i}",
                min_value=0,
                max_value=10000
                )
            
        with col4:
            st.session_state['legs'][i]['premium'] = st.number_input(
                "Premium", 
                value = leg["premium"],
                key=f"premium_{i}",
                min_value=0,
                max_value=1000
                )


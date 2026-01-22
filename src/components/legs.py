import streamlit as st

def render_legs():
    """ Render Option Leg Inputs """
    col1, col2, col3, col4 = st.columns([0.3,0.3,0.2,0.2])

    legs = st.session_state['legs']
    for i, leg in enumerate(legs):
        with col1:
            st.session_state['legs'][i]['option_type'] = st.selectbox(
                f"Option Type {i+1}", 
                ["Call","Put"],
                index = 1 if leg['option_type'] == "Put" else 0,
                key=f"option_type_{i}"
                )
            
        with col2:
            st.session_state['legs'][i]['direction'] = st.selectbox(
                "Direction", 
                ["Long","Short"], 
                index = 1 if leg['direction'] == "Short" else 0,
                key=f"option_direction_{i}"
                )

        with col3:
            st.session_state['legs'][i]['strike'] = st.number_input(
                "Strike Price", 
                value = float(leg["strike"]),
                key=f"strike_{i}",
                step = 0.5,
                min_value=0.0,
                max_value=10000.0
                )
            
        with col4:
            st.session_state['legs'][i]['premium'] = st.number_input(
                "Premium", 
                value = float(leg["premium"]),
                key=f"premium_{i}",
                step = 0.5,
                min_value=0.0,
                max_value=10000.0
                )


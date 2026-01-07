import streamlit as st

def _handle_add_leg():
    if len(st.session_state.legs) < 10:
        st.session_state.legs.append({'option_type': 'call', 
                                    'direction': 'long', 
                                    'strike': 500, 
                                    'premium': 1})
    else:
        st.warning("You can only have up to 10 trades.")

def _handle_remove_leg():
    if len(st.session_state.legs) > 1:
        st.session_state.legs.pop()
    else:
        st.warning("You must have at least one trade.")


def render_toolbar():
    with st.container():
        col1, col2 = st.columns(2)

        with col1:
            st.button("Add Trade", on_click=_handle_add_leg, type="primary")
        
        with col2:
            st.button("Remove Trade", on_click=_handle_remove_leg)
        

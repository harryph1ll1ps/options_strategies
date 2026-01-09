import streamlit as st

def render_ai_summary():
    
    def _show_ai_summary():
        st.session_state.show_ai_summary = True

    st.button("AI Summary", on_click=_show_ai_summary, icon="🧠", key="summary_button")
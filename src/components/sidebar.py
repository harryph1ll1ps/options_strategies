import streamlit as st

def render_sidebar():
    sidebar_what_are_options()
    sidebar_how_to_use()
    sidebar_faq()
    sidebar_about()
    sidebar_more()


def sidebar_what_are_options():
    st.sidebar.markdown('### What are options?')
    st.sidebar.markdown('Blah blah blah')
    st.sidebar.markdown('Blah blah blah')
    st.sidebar.markdown('---')


def sidebar_how_to_use():
    st.sidebar.markdown('### How to use this strategy builder?')
    st.sidebar.markdown('Blah blah blah')
    st.sidebar.markdown('Blah blah blah')
    st.sidebar.markdown('---')

def sidebar_faq():
    st.sidebar.markdown('### FAQs about strategy building')
    st.sidebar.markdown('Blah blah blah')
    st.sidebar.markdown('Blah blah blah')
    st.sidebar.markdown('---')  

def sidebar_about():
    st.sidebar.markdown('### About')
    st.sidebar.markdown('No data is stored or saved')
    st.sidebar.markdown('---')

def sidebar_more():
    st.sidebar.markdown('### More')
    st.sidebar.markdown('[Suggest Improvements or Report Issues](www.google.com)')
    st.sidebar.markdown('[Made by Harry](www.google.com)')
    st.sidebar.markdown('---')
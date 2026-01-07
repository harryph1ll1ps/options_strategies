import streamlit as st
from src.components.header import render_head
from src.components.store import configure_store
from src.components.sidebar import render_sidebar
from src.components.legs import render_legs
from src.components.toolbar import render_toolbar
from src.components.slider import render_slider
from src.components.payoff import render_payoff

render_head()

configure_store()

render_sidebar()

render_legs()

render_toolbar()

render_slider()

render_payoff()
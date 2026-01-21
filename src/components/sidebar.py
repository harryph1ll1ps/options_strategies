import streamlit as st
import textwrap


def render_sidebar():
    sidebar_how_to_use()
    sidebar_faq()
    sidebar_about()
    sidebar_more()


def sidebar_how_to_use():
    st.sidebar.markdown('## How to use the strategy builder?')
    st.sidebar.markdown(textwrap.dedent("""
    There are ***three key steps*** to using the options strategy builder:

    1. **Select Legs:** Build the individual trade legs that make up your strategy
    2. **Analyse Payoff:** View the payoff across different expiry prices and visualise it using an automatically generated payoff diagram
    3. **AI Analysis:** Generate an AI summary that explains the risk, reward, and intent of your strategy
    """))
    st.sidebar.markdown('---')

def sidebar_faq():
    st.sidebar.markdown("""## Frequently Asked Questions (FAQs)""")
    st.sidebar.markdown('`What are options?`')
    st.sidebar.markdown("""
                        Options are financial contracts that work a lot like insurance.

                        When you buy house insurance, you pay a premium for the right to be protected if something goes wrong, but you are not forced to make a claim. Options work the same way. You pay a premium for the right, but not the obligation, to buy or sell an asset at a fixed price before (or on) a certain expiry date.
                        """)
    st.sidebar.markdown('`What is the difference between a call vs put?`')
    st.sidebar.markdown("""
                        A ***call option*** gives you the right to buy an asset at a fixed price before a certain date. You use a call when you expect the price of the asset to rise.

                        A ***put option*** gives you the right to sell an asset at a fixed price before a certain date. You use a put when you expect the price of the asset to fall.
                        """)
    st.sidebar.markdown('`What is the difference between going long vs short?`')
    st.sidebar.markdown("""
                        Going ***long*** means you buy an options contract and pay a premium. By going long, you receive a right but not an obligation to buy or sell the underlying asset, depending on whether the option is a call or a put.

                        Going ***short*** means you sell an options contract and receive a premium. By going short, you take on an obligation to buy or sell the underlying asset if the option holder chooses to exercise.
                        """)
    st.sidebar.markdown('`What is a premium?`')
    st.sidebar.markdown("""
                        The ***premium*** is the price paid to buy an options contract and the income received for selling one.
                        """)
    st.sidebar.markdown('`What is a strike price?`')
    st.sidebar.markdown("""
                        The ***strike price*** is the fixed price at which the underlying asset can be bought or sold if the option is exercised.
                        """) 
    st.sidebar.markdown('`What is a spot price?`')
    st.sidebar.markdown("""
                        The ***spot price*** is the current market price of the underlying asset.
                        """)
    st.sidebar.markdown('---')


def sidebar_about():
    st.sidebar.markdown('## About')
    st.sidebar.markdown('No data is stored or saved')
    st.sidebar.markdown('---')

def sidebar_more():
    st.sidebar.markdown('## More')
    st.sidebar.markdown('[Suggest Improvements or Report Issues](https://github.com/harryph1ll1ps/options_strategies/issues/new)')
    st.sidebar.markdown('[Made by Harry](https://github.com/harryph1ll1ps)')
    st.sidebar.markdown('---')
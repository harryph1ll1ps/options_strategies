import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from src.utils.calculation import calculate_leg_return
import math


def generate_chart_lines(legs: list[dict], min_price: int, max_price: int):
    spot_prices = np.arange(min_price, max_price + 1)

    all_leg_returns = []

    for leg in legs:
        leg_returns = []

        # calculate the leg payoff at each spot price in the interval
        for spot in spot_prices:
            _, net_payoff = calculate_leg_return(leg, spot)
            leg_returns.append(net_payoff)

        all_leg_returns.append(leg_returns)

    return spot_prices, np.array(all_leg_returns)

def create_diagram(spot_prices, all_leg_returns):
    fig, ax = plt.subplots(figsize=(10, 6))

    # Plot individual legs
    for i, leg_returns in enumerate(all_leg_returns):
        ax.plot(
            spot_prices,
            leg_returns,
            linestyle="--",
            alpha=0.6,
            label=f"Leg {i + 1}",
        )

    # Plot the aggregate (strategy) return
    strategy_returns = np.sum(all_leg_returns, axis=0)

    ax.plot(
        spot_prices,
        strategy_returns,
        color="black",
        linewidth=3,
        label="Strategy",
    )

    # Zero line
    ax.axhline(0)
    ax.set_xlabel("Underlying Price at Expiry")
    ax.set_ylabel("Profit / Loss")
    ax.set_title("Options Payoff Diagram")
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)


def render_payoff_diagram():
    def _show_payoff_diagram():
        st.session_state.show_payoff_diagram = True

    def _hide_payoff_diagram():
        st.session_state.show_payoff_diagram = False

    st.markdown("")

    if not st.session_state.show_payoff_diagram:
        st.button("Show Chart", on_click=_show_payoff_diagram, icon="📈", key="payoff_diagram_button")

    if st.session_state.show_payoff_diagram:
        st.button("Close Chart", on_click=_hide_payoff_diagram, icon="❌", key="payoff_diagram_exit_button")

        with st.spinner('loading data...'):
            spot_prices, lines = generate_chart_lines(
                legs=st.session_state.legs,
                min_price=st.session_state.min_spot_price,
                max_price=st.session_state.max_spot_price,
            )

            create_diagram(spot_prices, lines)
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from src.utils.math import calculate_leg_return


# DO SOME MORE WORK TO GET A REASONABLE MIN MAX AND STEP AUTOMATICALLY
# E.G +/- 5 pct of avg strike price
# PAYOFF DIAGRAM SHOULD BE THE MAIN FEATURE
# Put the spot price slider below



  


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

    def _get_intervals():
        strike_total = 0
        for leg in st.session_state.legs:
            strike = leg["strike"]
            strike_total += strike
        
        avg = strike_total / len(st.session_state.legs)

        upper = int(avg * 1.05)
        lower = int(avg * 0.95)

        return lower, upper

    st.markdown('### More Tools')
    st.button("Payoff Diagram", on_click=_show_payoff_diagram, icon="📈", key="payoff_diagram_button")

    lower, upper = _get_intervals()

    if st.session_state.show_payoff_diagram:
        col1, col2 = st.columns(2)

        with col1:
            st.session_state.min_spot_price = st.number_input(
                "Min Spot Price", 
                value = lower,
                key=f"min_spot_price_input",
                min_value=0,
                max_value=10000
                )            
        
        with col2:
            st.session_state.max_spot_price = st.number_input(
                "Max Spot Price", 
                value = upper,
                key=f"max_spot_price_input",
                min_value=0,
                max_value=10000
                )     

        # with col3:
        #     st.session_state.spot_price_step = st.number_input(
        #         "Intervals", 
        #         value = st.session_state.spot_price_step,
        #         key=f"spot_price_step_input",
        #         min_value=0,
        #         max_value=500
        #         )    

        spot_prices, lines = generate_chart_lines(
            legs=st.session_state.legs,
            min_price=st.session_state.min_spot_price,
            max_price=st.session_state.max_spot_price,
            # step=st.session_state.spot_price_step,
        )

        create_diagram(spot_prices, lines)
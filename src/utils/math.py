def calculate_legs_return(legs, asset_price):
    """Calculate payoff for all legs"""

    total_payoff = 0.0
    total_net_payoff = 0.0

    for leg in legs:
        option_type = leg["option_type"]
        direction = leg["direction"]
        strike = leg["strike"]
        premium = leg["premium"]

        # intrinsic value (call vs put)
        if option_type == "Call":
            intrinsic = max(asset_price - strike, 0)
        else:
            intrinsic = max(strike - asset_price, 0)

        # direction (long vs short)
        if direction == "Long":
            payoff = intrinsic
            net_payoff = payoff - premium
        else: 
            payoff = -intrinsic
            net_payoff = -intrinsic + premium

        total_payoff += payoff
        total_net_payoff += net_payoff

    return total_payoff, total_net_payoff
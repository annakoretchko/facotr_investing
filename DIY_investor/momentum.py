


def get_momentum():

    """[The steps involved in capturing simple momentum]

    1. Identify investible universe; generally eliminate micro_cap firms
    2. For all firms in the universe, calculate the firm's cumulative return 
    over the past 12 months, ignoring the return from the last month. (this is the momentum variable)
    3. Rank all firms on momentum, and buy top decile. Equal weight 
    the firms selected. 
    4. Rebalance monthly. 


    """
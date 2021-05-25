import numpy as np
import pandas as pd
from datetime import datetime

dates = pd.date_range(datetime.strptime('10/10/2018', '%m/%d/%Y'), periods=11, freq='D')
close_prices = np.arange(len(dates))

close = pd.Series(close_prices, dates)
close

close.rolling(window = 3)

close.rolling(window = 3).sum()

close.rolling(window = 3).min()

def calculate_simple_moving_average(rolling_window, close):
    """
    Compute the simple moving average.
    
    Parameters
    ----------
    rolling_window: int
        Rolling window length
    close : DataFrame
        Close prices for each ticker and date
    
    Returns
    -------
    simple_moving_average : DataFrame
        Simple moving average for each ticker and date
    """
    # TODO: Implement Function
    
    return close.rolling(rolling_window).mean()
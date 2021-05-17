import numpy as np
import pandas as pd

def csv_to_close(csv_filepath, field_names):
    """
    Returns
    -------
    close : DataFrame
        Close prices for each ticker and date
    """
    
    price_df = pd.read_csv(csv_filepath, names=field_names)

    close_prices = price_df.pivot(index='date', columns='ticker', values='close')
    
    print(close_prices)
    
    return close_prices
    
def days_to_weeks(open_prices, high_prices, low_prices, close_prices):
    """
    Returns
    -------
    open_prices_weekly : DataFrame
        Weekly open prices for each ticker and date
    high_prices_weekly : DataFrame
        Weekly high prices for each ticker and date
    low_prices_weekly : DataFrame
        Weekly low prices for each ticker and date
    close_prices_weekly : DataFrame
        Weekly close prices for each ticker and date
    """
    # print(open_prices.resample('W').first())
    
    return open_prices.resample('W').first(),high_prices.resample('W').high(), low_prices.resample('W').last(), close_prices.resample('W').last()


dates = pd.date_range('10/10/2018', periods=11, freq='D')
close_prices = np.arange(len(dates))

close = pd.Series(close_prices, dates)
close
import pandas as pd

month = pd.to_datetime('02/01/2018')
close_month = pd.DataFrame(
    {
        'A': 1,
        'B': 12,
        'C': 35,
        'D': 3,
        'E': 79,
        'F': 2,
        'G': 15,
        'H': 59},
    [month])

def get_top_n(prev_returns, top_n):
    """
    Select the top performing stocks

    Parameters
    ----------
    prev_returns : DataFrame
        Previous shifted returns for each ticker and date
    top_n : int
        The number of top performing stocks to get

    Returns
    -------
    top_stocks : DataFrame
        Top stocks for each ticker and date marked with a 1
    """
    # TODO: Implement Function
    retVal = prev_returns.copy()
    retVal.loc[:,:] = 0

    for index, row in prev_returns.iterrows():
        winners = prev_returns.loc[index].nlargest(top_n)
        for win in winners.index:
            retVal.loc[index][win] = 1

    return retVal.astype('int64')

def date_top_industries(prices, sector, date, top_n):
    """
    Get the set of the top industries for the date

    Parameters
    ----------
    prices : DataFrame
        Prices for each ticker and date
    sector : Series
        Sector name for each ticker
    date : Date
        Date to get the top performers
    top_n : int
        Number of top performers to get

    Returns
    -------
    top_industries : set
        Top industries for the date
    """
    top = prices.loc[date].nlargest(top_n)

    bottom = (-1 * prices.loc[date].nlargest(2)) *-1


    return set(sector.loc[top.index])


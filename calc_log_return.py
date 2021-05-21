import pandas as pd

close = pd.DataFrame(
    {
        'ABC': [1, 5, 3, 6, 2],
        'EFG': [12, 51, 43, 56, 22],
        'XYZ': [35, 36, 36, 36, 37],},
    pd.date_range('10/01/2018', periods=5, freq='D'))

def calculate_returns(close):
    """Returns
    -------
    returns : DataFrame
        Returns for each ticker and date
    """
    # RETURN = Pt -Pt-1/Pt
    return (close - close.shift(1))/close.shift()

def compute_log_returns(prices):
    """
    Compute log returns for each ticker.

    Parameters
    ----------
    prices : DataFrame
        Prices for each ticker and date

    Returns
    -------
    log_returns : DataFrame
        Log returns for each ticker and date
    """
    # R = log(Pt) - log(Pt-1)
    return np.log(prices) - np.log(prices.shift(1))

def shift_returns(returns, shift_n):
    """
    Generate shifted returns

    Parameters
    ----------
    returns : DataFrame
        Returns for each ticker and date
    shift_n : int
        Number of periods to move, can be positive or negative

    Returns
    -------
    shifted_returns : DataFrame
        Shifted returns for each ticker and date
    """
    # TODO: Implement Function

    return returns.shift(shift_n)

quiz_tests.test_calculate_returns(calculate_returns)
import yfinance as yf
import pandas as pd


def download_data(ticker: str = 'TSLA') -> pd.DataFrame:
    """
    Download historical price data for a given stock ticker using yfinance.

    Parameters
    ----------
    ticker : str, optional
        Stock ticker symbol to download data for (default is 'TSLA').

    Returns
    -------
    pd.DataFrame
        A DataFrame containing historical price data with the date as a column.
    """

    df = yf.download(
        ticker,
        period='max',
        multi_level_index=False
    ).reset_index()

    return df

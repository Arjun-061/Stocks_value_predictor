from pathlib import Path
import yfinance as yf
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)

DATA_FILE = DATA_DIR / "stock_data.csv"


def fetch_stock_data(ticker="AAPL", period="5y"):
    print(f"Downloading data for {ticker}...")

    df = yf.download(
        ticker,
        period=period,
        auto_adjust=True,
        group_by="column"
    )

    # Flatten MultiIndex columns if present
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)

    df.reset_index(inplace=True)

    df.to_csv(DATA_FILE, index=False)

    print(f"Data saved to: {DATA_FILE}")

    return df
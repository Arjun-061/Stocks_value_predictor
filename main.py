from src.data_loader import fetch_stock_data
from src.train_model import train
from src.predict import predict


def main():
    ticker = input(
        "Enter Stock Symbol (Example: AAPL, TSLA, MSFT): "
    ).upper()

    fetch_stock_data(ticker)

    train()

    predict()


if __name__ == "__main__":
    main()
from pathlib import Path
import pandas as pd
import pickle

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_FILE = BASE_DIR / "data" / "stock_data.csv"
MODEL_FILE = BASE_DIR / "models" / "model.pkl"


def predict():
    with open(MODEL_FILE, "rb") as f:
        model = pickle.load(f)

    df = pd.read_csv(DATA_FILE)

    latest_data = df[["Open", "High", "Low", "Volume"]].iloc[-1:]

    prediction = model.predict(latest_data)

    print(
        f"Predicted Next Closing Price: ${prediction[0]:.2f}"
    )

    return prediction[0]
from pathlib import Path
import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_FILE = BASE_DIR / "data" / "stock_data.csv"

MODEL_DIR = BASE_DIR / "models"
MODEL_DIR.mkdir(exist_ok=True)

MODEL_FILE = MODEL_DIR / "model.pkl"


def train():
    df = pd.read_csv(DATA_FILE)
    # print("\nColumns:")
   # print(df.columns)

   # print("\nFirst 5 rows:")
   # print(df.head())

   # print("\nData Types:")
   # print(df.dtypes)

    df = df.dropna()

    X = df[["Open", "High", "Low", "Volume"]]
    y = df["Close"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    model = LinearRegression()

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    accuracy = r2_score(y_test, predictions)

    print(f"Model Accuracy (R²): {accuracy:.4f}")

    with open(MODEL_FILE, "wb") as f:
        pickle.dump(model, f)

    print(f"Model saved to: {MODEL_FILE}")

    return accuracy
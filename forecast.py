import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import TimeSeriesSplit


def make_train_test(df: pd.DataFrame):
    df = df.sort_values('date')

    n_splits = int(1 / 0.2) 

    tscv = TimeSeriesSplit(n_splits=n_splits)
    train_idx, test_idx = next(tscv.split(df))

    train = df.iloc[train_idx]
    test = df.iloc[test_idx]

    return train, test


if __name__ == "__main__":
    # Charger les données (ton fichier)
    df = pd.read_csv("data.csv", parse_dates=["date"])
    # Modèle "jouet" pour illustrer (au besoin, supprime si inutile)
    train, test = make_train_test(df)
    model = LinearRegression()
    model.fit(train[["sales"]], train["sales"])
    score = model.score(test[["sales"]], test["sales"])
    print(f"Score test (buggué, fuite possible): {score:.3f}")
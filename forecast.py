import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import TimeSeriesSplit


def make_train_test(df: pd.DataFrame):
    """
    BUG: split aléatoire sans respecter le temps -> fuite de données.
    """
    # Mélange les dates passées et futures => data leakage
    train, test = train_test_split(df, test_size=0.2, random_state=42, shuffle=True)
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
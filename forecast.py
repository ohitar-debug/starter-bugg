import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


def make_train_test(df: pd.DataFrame):
    """
    BUG: split aléatoire sans respecter le temps -> fuite de données.
    """
    # Mélange les dates passées et futures => data leakage
    df = df.sort_values('date', ascending=True)
    split_index = int(len(df) * (0.8))

    train = df.iloc[:split_index]
    test = df.iloc[split_index:]

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
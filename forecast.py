import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import TimeSeriesSplit


def make_train_test(df: pd.DataFrame , test_size = 0.2):
    """
    BUG: split aléatoire sans respecter le temps -> fuite de données.
    """
    # Mélange les dates passées et futures => data leakage
    df = df.sort_values('date')

    # Calculer l'index de séparation
    split_index = int(len(df) * (1 - test_size))

    train = df.iloc[:split_index]
    test = df.iloc[split_index:]
    return train, test


if __name__ == "__main__":
    # Charger les données
    df = pd.read_csv("data.csv", parse_dates=["date"])
    # Split temporel
    train, test = make_train_test(df, test_size=0.2)
    # Exemple de modèle
    model = LinearRegression()
    model.fit(train[["sales"]], train["sales"])
    score = model.score(test[["sales"]], test["sales"])
    print(f"Score test (sans fuite de données): {score:.3f}")
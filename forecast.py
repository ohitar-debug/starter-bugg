import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import TimeSeriesSplit


# def make_train_test(df: pd.DataFrame):
#     """
#     BUG: split aléatoire sans respecter le temps -> fuite de données.
#     """
#     # Mélange les dates passées et futures => data leakage
#     train, test = train_test_split(df, test_size=0.2, random_state=42, shuffle=True)
#     return train, test

# SOLUTION 1: séparation temporelle

# def make_train_test(df: pd.DataFrame, test_size: float = 0.2):
#     """
#     Sépare les données sans les mélanger aléatoirement pour respecter l’ordre temporel.
#     """
#     df_sorted = df.sort_values("date")
#     split_index = int(len(df_sorted) * (1 - test_size))
#     train = df_sorted.iloc[:split_index]
#     test = df_sorted.iloc[split_index:]
#     return train, test

# SOLUTION 2 avec les quantiles

def make_train_test(df: pd.DataFrame, test_size: float = 0.2):
    """
    Sépare les données temporellement en utilisant le quantile de la colonne 'Date'
    pour éviter le mélange aléatoire et respecter l’ordre temporel.
    """
    # S'assurer que la colonne Date est au bon format
    df = df.copy()
    df["Date"] = pd.to_datetime(df["date"])

    # Calcul de la date seuil à partir du quantile
    split_date = df["Date"].quantile(1 - test_size)

    # Split chronologique
    train = df[df["Date"] < split_date]
    test = df[df["Date"] >= split_date]
    return train, test



if __name__ == "__main__":
    # Charger les données (ton fichier)
    df = pd.read_csv("data.csv", parse_dates=["date"])
    # Modèle "jouet" pour illustrer (au besoin, supprime si inutile)
    train, test = make_train_test(df)
    model = LinearRegression()
    model.fit(train[["sales"]], train["sales"])
    score = model.score(test[["sales"]], test["sales"])
    print(f"Score test reussi: {score:.3f}")
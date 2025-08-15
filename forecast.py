import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import TimeSeriesSplit




def make_train_test(df: pd.DataFrame):
    """
    Split temporel 80/20 : toutes les dates de test sont postérieures à celles de train.
    Hypothèse : df contient 'date' de type datetime.
    """
    df_sorted = df.sort_values("date").reset_index(drop=True)
    cutoff = int(len(df_sorted) * 0.8)
    train = df_sorted.iloc[:cutoff]
    test  = df_sorted.iloc[cutoff:]
    return train, test



if __name__ == "__main__":
    # Charger les données (ton fichier)
    df = pd.read_csv("data.csv", parse_dates=["date"])
    # Modèle "jouet" pour illustrer (au besoin, supprime si inutile)
    train, test = make_train_test(df)
    model = LinearRegression()
    model.fit(train[["sales"]], train["sales"])  # (exemple bête : identity)
    score = model.score(test[["sales"]], test["sales"])
    print(f"Score test (buggué, fuite possible): {score:.3f}")

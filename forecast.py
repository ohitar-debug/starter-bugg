# forecast.py — VERSION BUGGÉE (intentionnellement)
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import TimeSeriesSplit


import pandas as pd
from forecast import make_train_test

def test_no_data_leakage_on_dates():
    """
    Le test est VERT si TOUTES les dates de test sont postérieures à TOUTES les dates de train.
    Avec le split aléatoire, ce test DOIT échouer (ROUGE).
    """
    # Génère un DF simple directement depuis data.csv pour coller au vrai schéma
    df = pd.read_csv("data.csv", parse_dates=["date"])

    train, test = make_train_test(df)

    assert test["date"].min() > train["date"].max(), \
        "Fuite de données détectée : le split n'est pas temporel (dates train/test se chevauchent)."


if __name__ == "__main__":
    # Charger les données (ton fichier)
    df = pd.read_csv("data.csv", parse_dates=["date"])
    # Modèle "jouet" pour illustrer (au besoin, supprime si inutile)
    train, test = make_train_test(df)
    model = LinearRegression()
    model.fit(train[["sales"]], train["sales"])  # (exemple bête : identity)
    score = model.score(test[["sales"]], test["sales"])
    print(f"Score test (buggué, fuite possible): {score:.3f}")

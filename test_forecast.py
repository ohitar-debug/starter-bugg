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
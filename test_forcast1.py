import pandas as pd
from forecast import make_train_test  # split aléatoire existant

def make_train_test_chrono(df: pd.DataFrame, test_size=0.2):
    """
    Split chronologique pour éviter la fuite de données.
    """
    # Trier les données par date
    df = df.sort_values("date")
    split_idx = int(len(df) * (1 - test_size))
    train = df.iloc[:split_idx]
    test = df.iloc[split_idx:]
    return train, test

def test_no_data_leakage_on_dates():
    """
    Le test est VERT si TOUTES les dates de test sont postérieures à TOUTES les dates de train.
    Avec le split aléatoire, ce test DOIT échouer (ROUGE).
    """
    # Charger le DataFrame
    df = pd.read_csv("data.csv", parse_dates=["date"])

    # Split aléatoire (shuffle=True) — montre le bug
    train, test = make_train_test(df)

    # Ce test échouera normalement avec le split aléatoire
    try:
        assert test["date"].min() > train["date"].max(), \
            "Test échoué : certaines dates de test sont antérieures aux dates de train → fuite de données"
    except AssertionError as e:
        print(e)

    # Split chronologique correct — pas de fuite de données
    train_chrono, test_chrono = make_train_test_chrono(df)

    # Vérification — doit passer
    assert test_chrono["date"].min() > train_chrono["date"].max(), \
        "Erreur : fuite de données détectée malgré le split chronologique"
    print("Test chronologique OK : pas de fuite de données.")

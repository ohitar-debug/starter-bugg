import pandas as pd
from forecast import make_train_test

def test_no_data_leakage_on_dates():
   
    # Génère un DF simple directement depuis data.csv pour coller au vrai schéma
    df = pd.read_csv("data.csv", parse_dates=["date"])

    train, test = make_train_test(df)

    assert test["date"].min() > train["date"].max(), \
        "m"
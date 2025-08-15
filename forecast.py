import pandas as pd
from sklearn.linear_model import LinearRegression



def make_train_test(df: pd.DataFrame, train_ratio: float = 0.8):
    
     # Tri par date
    df= df.sort_values(by="date").reset_index(drop=True)

    # Calcul de l'index de séparation (80% train, 20% test)
    split_index = int(len(df) * train_ratio)

    # Découpage chronologique
    train = df.iloc[:split_index]
    test = df.iloc[split_index:]

    return train, test


if __name__ == "__main__":
    # Charger les données (ton fichier)
    df = pd.read_csv("data.csv", parse_dates=["date"])
    # Modèle "jouet" pour illustrer (au besoin, supprime si inutile)
    # Séparation train/test
    train, test = make_train_test(df, train_ratio=0.8)

    model = LinearRegression()
    model.fit(train[["sales"]], train["sales"])
    score = model.score(test[["sales"]], test["sales"])
    print(f"Score test (buggué, fuite possible): {score:.3f}")
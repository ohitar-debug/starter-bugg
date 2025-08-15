# 🧪 TP : Découverte de GitHub Actions

Dans ce TP, nous allons utiliser GitHub Actions pour exécuter automatiquement les tests Python à chaque `push` ou `pull request`.

---

## 🚀 Instructions rapides

```bash
# 1. Cloner et installer
git clone https://github.com/ohitar-debug/starter-bugg.git
cd starter-bugg
python -m venv .venv && . .venv/Scripts/Activate.ps1  # mac: source .venv/bin/activate
pip install -r requirements.txt

# 2. Créer branche + introduire un bug
git checkout -b demo/bug
# (modifier forecast.py pour réintroduire le split aléatoire :
# remplacer le split temporel par un train_test_split(..., shuffle=True))
pytest -v && git add . && git commit -m "bug demo" && git push -u origin demo/bug

# 3. Corriger + push
# (réparer forecast.py en remettant un split temporel basé sur la date)
pytest -v && git commit -am "fix" && git push




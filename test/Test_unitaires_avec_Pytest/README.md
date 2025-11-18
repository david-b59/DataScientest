
---

# ✅ ** `Test_unitaires_avec_Pytest/`**  


# 🧪 Tests Unitaires avec Pytest

Ce dossier contient les exercices du module **Tests Unitaires** réalisés avec `pytest`.  
L’objectif était d’apprendre à valider le comportement d’unité de code de manière fiable et automatisée.

---

## 📘 Concepts abordés

- `assert` pour vérifier les résultats attendus  
- organisation des fichiers `xxx.py` et `xxx_test.py`
- utilisation de `pytest.raises()` pour tester les exceptions
- introduction aux **fixtures**
- tests paramétrés
- bonnes pratiques d’écriture de tests

---

## 📁 Fichiers présents

Test_unitaires_avec_Pytest/

├── code1.py           # fonction total()

├── code1_test.py      # tests unitaires associés

├── wallet.py          # classe Wallet + exception InsufficientAmount

└── wallet_test.py     # tests unitaires complets de Wallet


---

## ▶️ Lancer les tests

Depuis le dossier `test/` :

```bash
pytest Test_unitaires_avec_Pytest/

# 🧪 Module Test — Exercices et Travaux Pratiques

Ce dossier regroupe l'ensemble des exercices liés aux tests (unitaire, paramétré, TDD) réalisés dans le cadre de ma formation DataScientest.  
Chaque sous-dossier correspond à un module ou à une séquence pédagogique spécifique.

## 📁 Structure du dossier

test/

├── Test_unitaire_avec_Pytest/

│ ├── code1.py

│ ├── code1_test.py

│ ├── wallet.py

│ └── wallet_test.py

│

├── Test_Driven_Development/

│ ├── bibliotheque.py

│ └── test_bibliotheque.py

│

└── exem_test_BAUDUIN/

├── note.txt

├── reponse.txt

└── exem_test_BAUDUIN.tar


---

## 📘 Contenu des sous-dossiers

### **🔹 Test_unitaires_avec_Pytest/**
Exercices portant sur :
- la création de tests unitaires avec `pytest`
- les assertions
- les fixtures
- les tests paramétrés
- la gestion des exceptions (`pytest.raises`)

Fichiers exemples :
- `code1.py`, `code1_test.py` → tests simples d’une fonction `total()`
- `wallet.py`, `wallet_test.py` → tests d'une classe avec exceptions personnalisées

---

### **🔹 Test_Driven_Development/**
Exercices du module TDD (Test Driven Development) :
- écriture des tests avant le code
- respect du cycle **RED → GREEN → REFACTOR**
- implémentation guidée par les tests

Exemples :
- Bibliothèque/livre avec ajout, suppression, recherche & statistiques

---

### **🔹 exem_test_BAUDUIN/**
Dossier d’exemple permettant :
- de manipuler des fichiers dans la VM  
- d’archiver un répertoire au format `.tar`  
- d’expérimenter le transfert VM → machine locale  
- utilisé comme support technique pour les futures évaluations

Ce dossier contient donc uniquement des essais de manipulation et d’archivage.

---

## ▶️ Exécuter les tests

Depuis la racine du dossier `test/` :

```bash
pytest nom_du_fichier_test.py

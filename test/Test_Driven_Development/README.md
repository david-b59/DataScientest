

# ✅ ** README 3 — pour `Test_Driven_Development/` **  

# 🔁 Test Driven Development (TDD)

Ce dossier rassemble les exercices du module **TDD — Test Driven Development**.  
L’objectif : apprendre à écrire le test *avant* d’écrire le code, en suivant le cycle :

## 🔄 Cycle TDD
1. **RED** : écrire un test qui échoue  
2. **GREEN** : écrire le minimum de code pour faire passer le test  
3. **REFACTOR** : améliorer et nettoyer le code  
4. **REPEAT** : ajouter de nouvelles fonctionnalités, recommencer le cycle  

---

## 📁 Fichiers présents

Test_Driven_Development/

├── bibliotheque.py # implémentation finale de l’exercice

└── test_bibliotheque.py # tests écrits en phase RED


---

## 📘 Exercices réalisés

- Création d’une classe `Livre`
- Création d’une classe `Bibliotheque` avec 5 fonctionnalités :
  - ajout de livre
  - suppression par titre
  - listing des livres
  - recherche par auteur
  - génération de statistiques (nombre, auteurs uniques)

Chaque fonctionnalité a été implémentée selon le cycle TDD.

---

## ▶️ Lancer les tests

```bash
pytest Test_Driven_Development/

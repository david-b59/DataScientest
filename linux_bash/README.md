# linux_bash

## 📝 Description

Ce dossier contient plusieurs scripts Bash créés dans le cadre du module **Fondamentaux de Linux & Bash (DataScientest)**.  
Il regroupe des exercices pratiques sur :

- l’écriture de scripts Bash,
- la manipulation de variables et de tableaux,
- les fonctions et structures de contrôle,
- l’automatisation de tâches avec `cron`.

---

## 📄 Contenu du dossier

### `test.sh`

#### Fonctionnalité

Script simple utilisé pour tester l'exécution automatique par **cron** :

- Ajoute une ligne horodatée dans `cron_log.txt` à chaque exécution.
- Permet de vérifier que le cron job fonctionne correctement.

#### Exemple de contenu

~~~bash
#!/bin/bash
echo "Cron Job exécuté à $(date)" >> /home/ubuntu/linux_bash/cron_log.txt
~~~

---

### `cron_log.txt`

#### Fonctionnalité

Fichier texte **généré automatiquement** par le script `test.sh` lorsqu’il est exécuté par `cron`.

- Contient l’historique des exécutions.
- Une nouvelle ligne est ajoutée à chaque exécution planifiée.

#### Exemple de contenu

~~~text
Cron Job exécuté à Mon Nov  3 17:05:01 UTC 2025
Cron Job exécuté à Mon Nov  3 17:06:01 UTC 2025
Cron Job exécuté à Mon Nov  3 17:07:01 UTC 2025
...
~~~

Ce fichier n’est pas modifié manuellement : il sert uniquement de **log**.

---

### `script.sh`

#### Fonctionnalité

Script d'entraînement complet regroupant les notions vues dans le cours :

- shebang (`#!/bin/bash`)
- variables et chaînes de caractères
- opérations arithmétiques
- tableaux
- boucles (`for`, `while`)
- conditions (`if`, `elif`, `else`)
- fonctions et arguments

#### Exemple de contenu

~~~bash
#!/bin/bash

# Variable simple
my_variable="hello world"
echo "$my_variable"

# Opérations arithmétiques
a=$((5 + 3))
b=$((a * 2))
echo "a = $a, b = $b"

# Tableau et boucle
prenoms=("Alice" "Bob" "Claire" "Daniel")

saluer() {
    local nom=$1
    echo "Bonjour, $nom !"
}

for prenom in "${prenoms[@]}"; do
    saluer "$prenom"
done
~~~

---

## 🔧 Automatisation via `cron`

Un cron job peut être configuré pour exécuter automatiquement le script `test.sh`.

#### Exemple d’entrée dans `crontab`

~~~text
*/1 * * * * /home/ubuntu/linux_bash/test.sh
~~~

- Exécute `test.sh` **toutes les minutes**.
- Ajoute une ligne dans `cron_log.txt` à chaque exécution.

---

## 🎯 Objectif pédagogique

Ce dossier permet de :

- pratiquer la création de scripts Bash ;
- manipuler variables, tableaux, boucles et conditions ;
- utiliser les permissions d’exécution (`chmod +x`) ;
- configurer des tâches planifiées via `crontab` ;
- analyser un fichier de logs généré automatiquement.

Il sert de base pour des scripts plus avancés :  
automatisation système, monitoring, orchestration, etc.

---

## 📌 Auteur

Travaux réalisés dans le cadre de la formation **Machine Learning Engineer — DataScientest**.

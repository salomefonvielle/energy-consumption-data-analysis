# Analyse de la consommation électrique par la Data Science

## Équipe

- Eduardo ROSA DE LIMA  
- Romero PERARDT MAGALHÃES BRITO  
- Salomé FONVIELLE  
- Otávio Higino MOURA DE ALENCAR  

---

## Objectif du projet

Ce projet vise à analyser et prédire la consommation électrique en Irlande à partir :

- de données météorologiques,
- de données de consommation électrique,
- sur une période de 518 jours,
- avec un pas de temps de 30 minutes.

L’objectif principal est de prévoir la consommation électrique sur un horizon de 15 jours à l’aide de différentes méthodes de Machine Learning.

---

## Données utilisées

Les données comprennent :

- Consommation électrique  
- Température, humidité, vent, rayonnement solaire  
- Indication des jours fériés  

### Étapes de préparation

1. Fusion des fichiers via la colonne `date`  
2. Interpolation à un pas de temps de 30 minutes  
3. Suppression des valeurs manquantes  
4. Étude des corrélations  
5. Réduction du nombre de variables  
6. Encodage cyclique du temps (sin/cos pour mois, heure, jour de semaine)  
7. Normalisation des variables  

Au final, quatre bases de données ont été construites :

- Base complète  
- Base complète normalisée  
- Base réduite  
- Base réduite normalisée  

---

## Modèles étudiés

Les modèles suivants ont été implémentés et comparés :

- Régression linéaire multidimensionnelle  
- Decision Tree  
- Random Forest  
- MLP (Multilayer Perceptron)  
- SARIMAX (modèle temporel avec variables exogènes)  
- Validation par validation glissante (Time Series Split) pour respecter la structure temporelle des données

---

## Résultats principaux

| Modèle | R² | MAPE |
|--------|----|------|
| Linear Regression | ~68% | ~25% |
| Decision Tree | ~88% | ~11% |
| Random Forest | ~93% | ~8% |
| MLP | ~92–94% | ~8–9% |
| SARIMAX | ~7% | ~30% |

Les modèles non linéaires (Random Forest et MLP) sont significativement plus performants que la régression linéaire et le modèle SARIMAX.

Le MLP offre un excellent compromis global, tandis que le Random Forest détecte plus finement les pics de consommation.

Une approche ensemble (moyenne MLP + Random Forest) a été utilisée pour produire la prédiction finale.

---

## Structure du projet

```text
energy-consumption-data-analysis/
│
├── data/
│   ├── raws/            # Données brutes
│   ├── processed/       # Données nettoyées / transformées
│   └── results/         # Prédictions exportées
│
├── notebooks/
│   ├── 01_data_preparation.ipynb
│   └── 02_models.ipynb
│
├── src/
│   ├── data_loader.py
│   ├── preprocessing.py
│   ├── feature_engineering.py
│   ├── validation.py
│   └── config.py
│
│
├── requirements.txt
└── README.md
```

---

## Installation

Créer un environnement virtuel :

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

---

## Exécution

1. Lancer le notebook de préparation des données :

`notebooks/01_data_preparation.ipynb`

2. Puis lancer le notebook de modélisation :

`notebooks/02_models.ipynb`

---

## Conclusion

La consommation électrique présente des dynamiques non linéaires complexes.  
Les modèles d’ensemble et les réseaux de neurones capturent efficacement ces relations.

L’approche finale repose sur une combinaison MLP + Random Forest afin d’obtenir une prédiction robuste et stable.

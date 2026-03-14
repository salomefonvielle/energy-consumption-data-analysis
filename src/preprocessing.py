"""
preprocessing.py — Fonctions de nettoyage et préparation des données.

Fournit :
- resample_and_interpolate : rééchantillonnage à 30 min + interpolation linéaire
- merge_on_datetime         : fusion de deux DataFrames sur colonne datetime
- extract_prediction_period : extraction d'une période de prédiction
- drop_missing_rows         : suppression des lignes avec valeurs manquantes
"""

import pandas as pd
import numpy as np


def resample_and_interpolate(
    df,
    date_col="date",
    numeric_cols=None,
    freq="30min",
    interpolation_method="linear"
):
    """
    Convertit la colonne date, resample la série temporelle
    à une fréquence fixe et interpole les colonnes numériques.

    Parameters
    ----------
    df : pd.DataFrame
    date_col : str
        Nom de la colonne date
    numeric_cols : list[str]
        Colonnes à convertir en numérique et à interpoler
    freq : str
        Fréquence temporelle (ex: '30min', '1H')
    interpolation_method : str
        Méthode d'interpolation (linear, time, spline...)

    Returns
    -------
    pd.DataFrame
        DataFrame resamplé et interpolé
    """

    df_copy = df.copy()

    # Conversion date
    df_copy[date_col] = pd.to_datetime(df_copy[date_col], errors="coerce")

    # Conversion numérique
    if numeric_cols is not None:
        df_copy[numeric_cols] = df_copy[numeric_cols].apply(
            pd.to_numeric, errors="coerce"
        )

    # Mise en index
    df_copy = df_copy.set_index(date_col)

    # Création nouvel index temporel
    new_index = pd.date_range(
        start=df_copy.index.min(),
        end=df_copy.index.max(),
        freq=freq
    )

    # Réindexation
    df_resampled = df_copy.reindex(new_index)

    # Interpolation
    df_resampled = df_resampled.interpolate(method=interpolation_method)

    # Reset index
    df_resampled = df_resampled.reset_index().rename(columns={"index": date_col})

    return df_resampled


def merge_on_datetime(
    df1,
    df2,
    date_col_df1="date",
    date_col_df2="date",
    how="inner"
):
    """
    Harmonise les colonnes date et fusionne deux DataFrames
    sur une colonne datetime.

    Returns
    -------
    pd.DataFrame
    """

    df1_copy = df1.copy()
    df2_copy = df2.copy()

    # Conversion en datetime
    df1_copy[date_col_df1] = pd.to_datetime(df1_copy[date_col_df1], errors="coerce")
    df2_copy[date_col_df2] = pd.to_datetime(df2_copy[date_col_df2], errors="coerce")

    # Harmonisation nom colonne
    if date_col_df1 != "date":
        df1_copy = df1_copy.rename(columns={date_col_df1: "date"})
    if date_col_df2 != "date":
        df2_copy = df2_copy.rename(columns={date_col_df2: "date"})

    merged_df = pd.merge(df1_copy, df2_copy, on="date", how=how)

    return merged_df


def extract_prediction_period(
    df,
    start_date,
    end_date=None
):
    """
    Extrait la période sur laquelle on souhaite faire des prédictions.
    """

    df_copy = df.copy()
    df_copy["date"] = pd.to_datetime(df_copy["date"])
    df_copy = df_copy.sort_values("date")

    start_date = pd.to_datetime(start_date)

    if end_date:
        end_date = pd.to_datetime(end_date) + pd.Timedelta(days=1)
        prediction_df = df_copy[
            (df_copy["date"] >= start_date) &
            (df_copy["date"] < end_date)
            ]
    else:
        prediction_df = df_copy[df_copy["date"] >= start_date]

    return prediction_df


def drop_missing_rows(df):
    """
    Reproduit exactement la logique :
    - affiche les valeurs manquantes
    - supprime toutes les lignes avec NaN
    - réaffiche les valeurs manquantes
    """

    missing_values = df.isnull().sum()
    print("Valeurs manquantes par colonne :")
    print(missing_values)

    df_cleaned = df.dropna()

    missing_values_after = df_cleaned.isnull().sum()
    print("Valeurs manquantes par colonne :")
    print(missing_values_after)

    return df_cleaned





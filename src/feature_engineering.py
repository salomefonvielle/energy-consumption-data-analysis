"""
feature_engineering.py — Création des features temporelles.

Applique un encodage cyclique (sin/cos) aux variables temporelles
(mois, heure, jour de semaine) afin de conserver leur structure circulaire.
"""

import numpy as np


def modulate_df(df):

    df['day_of_week'] = df['date'].dt.dayofweek
    df['hour'] = df['date'].dt.hour

    # Encodage cyclique
    df['month_sin'] = np.sin(2 * np.pi * df['month'] / 12)
    df['month_cos'] = np.cos(2 * np.pi * df['month'] / 12)
    df['hour_sin'] = np.sin(2 * np.pi * df['hour'] / 24)
    df['hour_cos'] = np.cos(2 * np.pi * df['hour'] / 24)
    df['day_of_week_sin'] = np.sin(2 * np.pi * df['day_of_week'] / 7)
    df['day_of_week_cos'] = np.cos(2 * np.pi * df['day_of_week'] / 7)

    df = df.drop(columns=[
        'hour', 'day_of_week',
        'year', 'month', 'day',
        'time', 'date'
    ])

    return df



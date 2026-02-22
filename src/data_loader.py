import pandas as pd
from pathlib import Path


def load_datasets(base_dir=None):
    """
    Charge les deux datasets principaux du projet.

    Paramètres
    ----------
    base_dir : Path or None
        Répertoire racine du projet.
        Si None, utilise le répertoire courant.

    Retour
    ------
    df1 : pd.DataFrame
    df2 : pd.DataFrame
    """

    if base_dir is None:
        base_dir = Path().resolve()

    data_path1 = base_dir / "data" / "df_vst_group5.csv"
    data_path2 = base_dir / "data" / "Corkstation_15072019_01022011.csv"

    df1 = pd.read_csv(data_path1)
    df2 = pd.read_csv(data_path2)

    return df1, df2
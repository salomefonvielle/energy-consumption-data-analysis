from pathlib import Path
import pandas as pd

def load_datasets(base_dir=None):
    """
    Charge les deux datasets principaux du projet.
    """

    if base_dir is None:
        # Racine du projet = parent du dossier src
        base_dir = Path(__file__).resolve().parent.parent

    data_path1 = base_dir / "data" / "raws"/"df_vst_group5.csv"
    data_path2 = base_dir / "data" / "raws"/"Corkstation_15072019_01022011.csv"

    df1 = pd.read_csv(data_path1)
    df2 = pd.read_csv(data_path2)

    return df1, df2

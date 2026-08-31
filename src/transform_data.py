import pandas as pd
from pathlib import Path
import json
import logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")



def create_dataframe(path_name:str) -> pd.DataFrame:
    path = path_name

    if not path.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {path}")

    with open(path) as f:
        data = json.load(f)

    df = pd.json_normalize(data)
    logging.info(f"DataFrame criado com sucesso: {df.shape[0]} linhas")
    return df  
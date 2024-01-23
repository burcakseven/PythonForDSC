import pandas as pd

def load(path: str) -> pd.DataFrame:
    Dataset = pd.read_csv(path)
    return Dataset


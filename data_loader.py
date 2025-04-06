import pandas as pd
import numpy as np

def load_volcano_data(filepath: str) -> pd.DataFrame:
    df = pd.read_excel(filepath, sheet_name="S4B limma results", skiprows=2)
    df = df[["logFC", "adj.P.Val", "EntrezGeneSymbol"]].dropna()
    df["-log10(adj.P.Val)"] = -np.log10(df["adj.P.Val"])
    return df

def load_expression_values(filepath: str) -> pd.DataFrame:
    df = pd.read_excel(filepath, sheet_name="S4A values", skiprows=2)
    return df
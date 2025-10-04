from pathlib import Path
import pandas as pd


def read_tsv(filepath: Path):
    df = pd.read_csv(
        filepath.resolve(),
        sep="\t",
        header=0,
    )
    return df


def read_ods(filepath: Path, sheet_name: int|str = 0):
    if not (filepath.is_file and filepath.suffix == ".ods"):
        raise ValueError(f"Invalid Open Document Spreadsheet: {filepath}")
    df = pd.read_excel(
        filepath.resolve(),
        sheet_name=sheet_name,
        engine="odf",
        header=0,
    )
    return df


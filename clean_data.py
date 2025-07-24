import pandas as pd
from typing import List


def clean_outcome_tables(outcome_tables: List[pd.DataFrame]):
    formatted_tables = [format_table(table) for table in outcome_tables]
    return formatted_tables


def format_table(outcome_df: pd.DataFrame):
    return outcome_df.to_dict(orient='records')

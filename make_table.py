import pandas as pd
from io import StringIO 


def get_fail_tables(fail_div_sections):
    tables = []
    for fail_div in fail_div_sections:
        raw_table = fail_div.find('table', class_='evidence')
        try:
            df = pd.read_html(StringIO(str(raw_table)))[0]
            if check_row(df, "No matching system items were found"):
                df = "NO TABLE DATA"
            tables.append(df)
        except ValueError:
            continue # skips if table is malformed
    return tables


def check_row(df: pd.DataFrame, filter_msg):
    return bool(df.apply(lambda row: row.astype(str).str.contains(filter_msg).any(), axis=1).any())




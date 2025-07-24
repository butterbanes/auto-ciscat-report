import itertools
import pandas as pd
import subprocess as sbp
import sys
from tabulate import tabulate as tbl
import threading
import time
from typing import Any, List

def display_loading_msg():
    loading_msg = 'Generating'
    bullets = itertools.cycle(['.','..','...'])
    while True:
        sys.stdout.write('\r' + (' '*(len(loading_msg)+3)) + '\r') # clear the current line
        sys.stdout.write(loading_msg + next(bullets)) # print loading message and iterate through bullets
        sys.stdout.flush()
        time.sleep(0.25)

def display_outcomes(outcomes: List[Any]):
    print(outcomes);

def display_assess_tables(assess_tables: List[Any]):
    formatted_assessments = [df.values.tolist() for df in assess_tables]
    print(tbl(formatted_assessments, tablefmt='grid'))

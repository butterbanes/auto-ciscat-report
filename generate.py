from datetime import datetime as dt
import os

def gen_timestamp():
    return dt.now().strftime('%Y-%m-%d_%H%M%S')

def auto_gen_name(filename):
    timestamp = gen_timestamp()
    base = os.path.splitext(filename)[0]
    base = base.replace('Microsoft_Windows_', 'MWin')
    name = f"{base}({timestamp})"
    return name

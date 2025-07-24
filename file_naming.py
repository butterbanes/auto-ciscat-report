import os
from datetime import datetime as dt

def extension_convert(filename: str, new_ext: str) -> str:
    base: str = os.path.splitext(filename)[0] # grabs the filename by itself without extension
    new_file_path: str = f"{base}.{new_ext.lstrip('.')}" # appends the new ext to the filename
    # remove the default -NonPassing portion from the CISCAT Assessor externally generated JSON files
    if ('-NonPassing') in new_file_path:
        new_file_path = new_file_path.replace('-NonPassing', '')
    return new_file_path

def clean_report_name(filename: str) -> str:
    filename = filename.replace('Microsoft_Windows_', 'MWin')
    extension = os.path.splitext(filename)[1] # grab the extension from the filename
    # ensure that filename is a docx file
    if not filename.endswith('.docx'):
        filename = filename.replace(extension, '.docx')
    return filename

def auto_gen_name(filename: str) -> str:
    timestamp = gen_timestamp()
    base = os.path.splitext(filename)[0]
    filename = f'{base}({timestamp})'
    return filename

def gen_timestamp():
    return dt.now().strftime('%Y-%m-%d_%H%M%S')

def has_file_extension(filename: str) -> bool:
    return bool(os.path.splitext(filename)[1])

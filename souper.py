from io import StringIO
from bs4 import BeautifulSoup as bs, Tag
import os
from bs4.element import PageElement
import pandas as pd
from typing import List, Sequence, Set
import re
from make_table import get_fail_tables
from parse_html import parse_html
from rule_parse import get_rule_titles
from setting_parse import get_rcmd_settings
from clean_data import clean_outcome_tables
from docxer import docx_writer


def souper(current_dir=os.getcwd()):
    """
    Takes the information from the html code and 'soups' it up using the
        bs4 BeautifulSoup library

    Params:
    current_dir(str): should always be your working directory

    Returns:
    BeautifulSoup: bs4 object returns by the bs4.BeautifulSoup class
    """
    html_code: str = parse_html(current_dir) # grab the html code
    soup = bs(html_code, 'html.parser') # parse the html tags/vars with the BeautifulSoup4 library
    fail_div_sections: Sequence[PageElement] = soup.find_all(attrs={'class': 'Rule resultRow'}) # list of PageElement objects present within the soup var
    rule_titles = get_rule_titles(fail_div_sections) # 
    outcomes_dict = get_rcmd_settings(fail_div_sections, rule_titles)
    flattened_outcomes: List[str] = [item for sublist in outcomes_dict.values() for item in sublist] # filters through dictionary values to grab section information
    flattened_outcomes_set = sorted(isolate_outcomes(flattened_outcomes), key=extract_section_number)

    outcome_tables = get_fail_tables(fail_div_sections)
    doc_name = docx_writer(flattened_outcomes_set, outcome_tables) 
    return doc_name


def isolate_outcomes(outcomes):
    """
    Original outcomes list contains mutiple values for each section, 
        this function isolates the longest one to contain the most 
        information relative to the section's suggested remediation

    Params:
    outcomes(List[str]): List of original outcomes with duplicate section numbers

    Returns:
    Set[str]: the outcomes with the longest structure relative to its section 
                number and its remediation suggestion
    """
    isolated_set: Set[str] = set()
    section_dict: dict[str, List[str]] = {}
    for outcome in outcomes:
        section_number = extract_section_number(outcome)
        if section_number != [-1, -1, -1, -1, -1]:
            section_key = '.'.join(str(number) for number in section_number[:5])
            if section_key not in section_dict:
                section_dict[section_key] = []
            section_dict[section_key].append(outcome)
    for section_group in section_dict.values():
        longest_outcome = max(section_group, key=len)
        isolated_set.add(longest_outcome)
    return isolated_set


def extract_section_number(outcome: str) -> List[int]:
    """
    Does what it says it does and isolates the section number from each section
        up to 5 decimal ranges (x.x.x.x.x) to account for even the deepest 
        sections

    Params:
    outcome(str): individual outcome to extract section number from

    Returns:
    List[str]: list containing the seperated parts of the section number
    """
    match = re.search(r'(\d+)\.(\d+)\.(\d+)\.(\d+)\.(\d+)', outcome) # uses regular expressions to search for the section number format
    if match:
        parts = match.groups()
        return [int(part) if part else -1 for part in parts]
    match = re.search(r'(\d+)\.(\d+)\.(\d+)\.(\d+)', outcome)
    if match:
        parts = match.groups()
        return [int(part) if part else -1 for part in parts] + [0]
    match = re.search(r'(\d+)\.(\d+)\.(\d+)', outcome)
    if match:
        parts = match.groups()
        return [int(part) if part else -1 for part in parts] + [0, 0]
    return [-1, -1, -1, -1, -1] # this is the default case if a section number isnt found


# ----------- DEBUG FUNCTIONS FOR TESTING ----------- #


def __DEBUG_PRINTS(some_list):
    for item in some_list:
        print(item)
        input('Press ENTER to view next item')


def __DEBUG_TAG_OUT_FILE(some_list):
    raw_html = ''.join(str(tag) for tag in some_list)
    with open('__DEBUG_TAG_FILE.TXT', 'w', encoding='utf-8') as DEBUG_FILE:
        DEBUG_FILE.write(raw_html)


def __DEBUG_OUT_FILE(some_list):
    with open('__DEBUG_FILE.TXT', 'w', encoding='utf-8') as DEBUG_FILE:
        for item in some_list:
            item += '\n'
            DEBUG_FILE.write(item)


souper()

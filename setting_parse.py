from typing import List, Set
import re


def get_rcmd_settings(fail_div_sections, rule_titles) -> dict[str, List[str]]:
    outcomes_list: List[str] = []
    outcomes_dict: dict[str, List[str]] = {}
    gp_config_msg: str = r'To establish the recommended configuration via GP, set the following UI path to'
    result: str = ""
    for fail_div, rule_title in zip(fail_div_sections, rule_titles):
        outcomes_set: Set[str] = set()
        # FIXME: its skipping certain portions BC they don't have span blocks
        for p_tag in fail_div.find_all('p'):
            tag_contents = ''.join(p_tag.stripped_strings)
            tag_contents = insert_after(tag_contents, 'path to', ' ')
            isolated_tag_str = insert_after(p_tag.find_next("p").get_text(strip=True), "path to", " ").split("Impact:", 1)[0]
            #print(f'{rule_title} | {isolated_tag_str}')
            if gp_config_msg or '\\' in isolated_tag_str:
                #print('----------------------INSIDE CONDITIONAL STATEMENT----------------------')
                span = p_tag.find('span', attrs={'class': 'inline_block'})
                if span:
                    span = span.get_text(strip=True)
                else:
                    # FIXME: need this conditional to get the skipped sections but it also grabs EVERYTHING
                    # FIXME: possible implemenation is to use a set per section and take the longest instance
                    span = ''
                code = p_tag.parent.parent.find_next('code', attrs={'class': 'code_block'})
                if code:
                    result = f'{gp_config_msg} {span}: {strip_excess_whitespace(code.get_text(strip=True))}'
                    result = f'{rule_title} <+=+> {result}'
                    outcomes_set.add(result)
                    outcomes_list.append(f'{result}') # right now we're only grabbing the resulting recommended GP config
            #print('----------------------OUTSIDE CONDITIONAL STATEMENT----------------------')
        #print(sorted(outcomes_set, reverse=True)[-1])
        outcomes_dict[rule_title] = outcomes_list
        #input('ENTER')
    return outcomes_dict


def insert_after(original, substring, to_insert):
    index = original.find(substring)
    if index != -1:
        index += len(substring)
        return original[:index] + to_insert + original[index:]
    return original


def strip_excess_whitespace(text):
    return re.sub(r'\s{2,}', ' ', text)

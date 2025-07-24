def get_rule_titles(fail_div_sections):
    rule_titles = []
    for fail_div in fail_div_sections:
        rule_titles.append(fail_div.find('h3', class_='ruleTitle').get_text())
    return rule_titles

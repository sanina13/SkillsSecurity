import re

list_regex = [r"you\s+are\s+now\s+a", r"forget\s+(everything|all)", r"act\s+as\s+(if\s+you\s+(were|are)|a|an)\s"]

def scan(text):
    findings = []

    functions_list = [override_attempt]

    for func in functions_list:
        result = func(text)
        if result is not None:
            findings.append(result)

    return findings

def override_attempt(text):
    list_lines = text.split("\n")
    for i, line in enumerate(list_lines):
        for reg in list_regex:
            matched = re.search(reg, line, re.IGNORECASE)
            if matched:
                matched_text = matched.group()
                return{
                    "rule": "role-override", "severity": "critical", "line": i + 1, "matched_text": matched_text
                }
    return None
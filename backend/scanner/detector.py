import re

def scan(text):
    findings = []

    functions_list = [override_attempt]

    for func in functions_list:
        result = func(text)
        if result is not None:
            findings.append(result)

    return findings

def override_attempt(text):
    list_regex = [r"you\s+are\s+now\s+a", r"forget\s+(everything|all)", r"act\s+as\s+(if\s+you\s+(were|are)|a|an)\s"]
    for reg in list_regex:
        if re.search(reg, text, re.IGNORECASE):
            return{
                "rule": "role-override", "severity": "critical"
            }
    return None
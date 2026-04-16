import re

LIST_REGEX_OVERRIDE = [r"you\s+are\s+now\s+a", r"forget\s+(everything|all)", r"act\s+as\s+(if\s+you\s+(were|are)|a|an)\s"]

LIST_SYSTEM_IMPERSONATION_REGEX = [r"\[\s*(system|admin|root)\s*\]", r"<<\s*(admin|system|root|override)\s*>>", r"developer\s+mode|admin\s+override|emergency\s+protocol"]

def scan(text):
    findings = []

    functions_list = [override_attempt, system_impersonation]

    for func in functions_list:
        result = func(text)
        if result is not None:
            findings.append(result)

    return findings

def override_attempt(text):
    list_lines = text.split("\n")
    for i, line in enumerate(list_lines):
        for reg in LIST_REGEX_OVERRIDE:
            matched = re.search(reg, line, re.IGNORECASE)
            if matched:
                matched_text = matched.group()
                return{
                    "rule": "role-override", "severity": "critical", "line": i + 1, "matched_text": matched_text
                }
    return None

def system_impersonation(text):
    list_lines = text.split("\n")

    for i, line in enumerate(list_lines):
        for reg in LIST_SYSTEM_IMPERSONATION_REGEX:
            matched = re.search(reg, line, re.IGNORECASE)
            if matched:
                matched_text = matched.group()
                return{
                   "rule": "system-impersonation", "severity": "critical", "line": i + 1, "matched_text": matched_text
                 }
    return None
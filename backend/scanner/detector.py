import re
from scanner.rules import RULES


def scan(text):
    findings = []
    lines = text.split("\n")

    for rule in RULES:
        for i, line in enumerate(lines):
            for pattern in rule["patterns"]:
                match = re.search(pattern, line, re.IGNORECASE)
                if match:
                    findings.append({
                        "rule": rule["id"],
                        "severity": rule["severity"],
                        "line": i + 1,
                        "matched_text": match.group(),
                        "line_content": line
                    })
    return findings


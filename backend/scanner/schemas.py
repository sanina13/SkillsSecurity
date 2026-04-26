from pydantic import BaseModel
from typing import List

class Finding(BaseModel):
    rule:str
    severity: str
    line: int
    matched_text: str
    line_content: str

class ScanSummary(BaseModel):
    critical: int
    high: int
    medium: int

class ScanResponse(BaseModel):
    filename: str
    total_findings: int
    summary: ScanSummary
    findings: List[Finding]


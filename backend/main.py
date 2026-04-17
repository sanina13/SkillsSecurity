from fastapi import FastAPI, UploadFile, HTTPException
from scanner.detector import scan

app = FastAPI()

@app.get("/")

def root():
    return {"message": "SkillSecurity API"}

@app.post("/scan")
async def scan_file(file: UploadFile):
    if not file.filename.endswith(".md"):
        raise HTTPException(status_code=400, detail="Only .md files are accepted")

    content = await file.read()

    if len(content) > 1_000_000:
            raise HTTPException(status_code=400, detail="File too large. Maximum size is 1MB")

    text = content.decode("utf-8")
    findings = scan(text)
    return {"filename": file.filename, "total_findings": len(findings), "summary": {
         "critical": sum(1 for find in findings if find.get("severity") == "critical"),
         "high": sum(1 for find in findings if find.get("severity") == "high"),
         "medium": sum(1 for find in findings if find.get("severity") == "medium")
    }, "findings": findings}












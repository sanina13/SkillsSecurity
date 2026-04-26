from fastapi import FastAPI, UploadFile, HTTPException
from scanner.detector import scan
from fastapi.middleware.cors import CORSMiddleware
from scanner.schemas import ScanResponse
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("skillsecurity")

app = FastAPI()

#Tells to FastApi to accept requests from localhost:5173
app.add_middleware(
     CORSMiddleware,
     allow_origins=["http://localhost:5173"],
     allow_methods=["*"],
     allow_headers=["*"]
)

@app.get("/")

def root():
    return {"message": "SkillSecurity API"}

@app.post("/scan", response_model=ScanResponse)
async def scan_file(file: UploadFile):
    if not file.filename.endswith(".md"):
        logger.warning("Rejected file: %s - invalid extension", file.filename)
        raise HTTPException(status_code=400, detail="Only .md files are accepted")

    content = await file.read()
    logger.info("Scan request: %s (%d bytes)", file.filename, len(content))
    if len(content) > 1_000_000:
            logger.warning("Rejected file: %s - too large (%d bytes)", file.filename, len(content))
            raise HTTPException(status_code=400, detail="File too large. Maximum size is 1MB")

    text = content.decode("utf-8")
    findings = scan(text)
    logger.info("Scan complete: %d findings", len(findings))
    return {"filename": file.filename, "total_findings": len(findings), "summary": {
         "critical": sum(1 for find in findings if find.get("severity") == "critical"),
         "high": sum(1 for find in findings if find.get("severity") == "high"),
         "medium": sum(1 for find in findings if find.get("severity") == "medium")
    }, "findings": findings}












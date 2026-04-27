from fastapi import FastAPI, UploadFile, HTTPException
from scanner.detector import scan
from fastapi.middleware.cors import CORSMiddleware
from scanner.schemas import ScanResponse
import logging
from dotenv import load_dotenv
import os

load_dotenv()

CORS_ORIGIN = os.getenv("CORS_ORIGIN", "http://localhost:5173")
MAX_FILE_SIZE = int(os.getenv("MAX_FILE_SIZE", 1000000))

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("skillsecurity")

app = FastAPI()

#Tells to FastApi to accept requests from localhost:5173
app.add_middleware(
     CORSMiddleware,
     allow_origins=[CORS_ORIGIN],
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
    if len(content) > MAX_FILE_SIZE:
        logger.warning("Rejected file: %s - too large (%d bytes)", file.filename, len(content))
        raise HTTPException(status_code=400, detail="File too large. Maximum size is 1MB")
    try:
        text = content.decode("utf-8")
    except UnicodeDecodeError:
        raise HTTPException(status_code=400, detail="File not valid in UTF-8")


    findings = scan(text)
    logger.info("Scan complete: %d findings", len(findings))
    return {"filename": file.filename, "total_findings": len(findings), "summary": {
         "critical": sum(1 for find in findings if find.get("severity") == "critical"),
         "high": sum(1 for find in findings if find.get("severity") == "high"),
         "medium": sum(1 for find in findings if find.get("severity") == "medium")
    }, "findings": findings}
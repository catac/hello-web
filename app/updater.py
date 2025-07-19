from fastapi import APIRouter, Header, HTTPException
from pydantic import BaseModel
import git
import os
import subprocess

update_router = APIRouter()

class UpdatePayload(BaseModel):
    update: bool

@update_router.post("/update_server")
async def update_server(
        info: UpdatePayload,
        authorization: str = Header(None)  # Optional header for authorization
    ):
    if authorization != "Token " + os.getenv("PA_API_TOKEN"):
        raise HTTPException(status_code=401, detail="Unauthorized")

    repo_dir = os.getenv("REPO_DIR")
    repo = git.Repo(repo_dir)
    origin = repo.remotes.origin
    if info.update:
        fi = origin.pull()
        process = subprocess.run(
            ["uv", "sync"],
            cwd=repo_dir,
            capture_output=True
        )
        exit_code = process.returncode
        result = {
            "message": "Code updated successfully", 
            "commit": fi[0].commit.hexsha + ": " + fi[0].commit.message.strip(),
            "uv_sync": process.stdout.decode('utf-8') + process.stderr.decode('utf-8') + f"Exit code: {exit_code}",
        }
    else:
        fi = origin.fetch()
        result = {
            "message": "No update performed",
            "commit": fi[0].commit.hexsha + ": " + fi[0].commit.message.strip(),
        }
    return result

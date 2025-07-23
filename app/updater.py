from fastapi import APIRouter, Header, HTTPException
from pydantic import BaseModel
import git
import os
import subprocess

update_router = APIRouter()


class UpdatePayload(BaseModel):
    update: bool


def get_commit_msg(commit):
    """Helper function to format commit message."""
    return f"{commit.hexsha}: {commit.message.strip()}"


def get_process_output(process):
    """Helper function to get output from a subprocess."""
    return (
        process.stdout.decode("utf-8")
        + process.stderr.decode("utf-8")
        + f"Exit code: {process.returncode}"
    )


@update_router.post("/update_server")
async def update_server(
    info: UpdatePayload,
    authorization: str = Header(None),  # Optional header for authorization
):
    pa_api_token = os.getenv("PA_API_TOKEN")
    if not pa_api_token or authorization != "Token " + pa_api_token:
        raise HTTPException(status_code=401, detail="Unauthorized")

    repo_dir = os.getenv("REPO_DIR")
    repo = git.Repo(repo_dir)
    origin = repo.remotes.origin
    if info.update:
        fi = origin.pull()
        process = subprocess.run(["uv", "sync"], cwd=repo_dir, capture_output=True)
        result = {
            "message": "Code updated successfully",
            "commit": get_commit_msg(fi[0].commit),
            "uv_sync": get_process_output(process),
        }
    else:
        fi = origin.fetch()
        result = {
            "message": "No update performed",
            "commit": get_commit_msg(fi[0].commit),
        }
    return result

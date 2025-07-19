from fastapi import FastAPI, Request
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

class Commit(BaseModel):
    id: str
    message: str
    timestamp: str
    url: str
    author: dict

class WebhookPayload(BaseModel):
    ref: str
    before: str
    after: str
    repository: dict
    pusher: dict
    commits: List[Commit]

@app.post("/update_server")
async def update_server(payload: WebhookPayload):
    # Trigger repo update logic here
    # Example: pull latest changes
    # repo = git.Repo('path/to/git_repo')
    # origin = repo.remotes.origin
    # origin.pull()
    return {"message": "Webhook received", "ref": payload.ref}

@app.get("/")
def read_root():
    return {"Hello": "World"}


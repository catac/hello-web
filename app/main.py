from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class UpdatePayload(BaseModel):
    update: bool

@app.post("/update_server")
async def update_server(info: UpdatePayload):
    # Trigger repo update logic here
    # Example: pull latest changes
    # repo = git.Repo('path/to/git_repo')
    # origin = repo.remotes.origin
    # origin.pull()
    return {
        "message": "Webhook received", 
        "payload": info.update
    }

@app.get("/")
def read_root():
    return {"Hello": "World"}


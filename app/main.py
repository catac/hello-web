from fastapi import FastAPI
import dotenv

dotenv.load_dotenv()
app = FastAPI()

from .updater import update_router
app.include_router(update_router)

@app.get("/")
def read_root():
    return {"Hello": "World"}

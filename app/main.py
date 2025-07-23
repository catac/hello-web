from fastapi import FastAPI
from updater import update_router
from prices import last_price

app = FastAPI()
app.include_router(update_router)


@app.get("/last_price/{symbol}")
async def get_last_price(symbol: str):
    price = last_price(symbol)
    return {"symbol": symbol, "price": price}


@app.get("/")
def read_root():
    return {"Hello": "World"}

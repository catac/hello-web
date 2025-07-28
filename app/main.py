from fastapi import FastAPI, HTTPException
from updater import update_router
from prices import last_price

app = FastAPI()
app.include_router(update_router)


@app.get("/last_price/{symbol}")
async def get_last_price(symbol: str):
    priceInfo = last_price(symbol)
    if priceInfo is None:
        raise HTTPException(
            status_code=404,
            detail="Price not available for the given symbol.",
        )
    return {
        "symbol": symbol,
        "price": priceInfo.price,
        "timestamp": priceInfo.timestamp.strftime("%Y-%m-%d %H:%M:%S %Z"),
    }


@app.get("/")
def read_root():
    return {"Hello": "World"}

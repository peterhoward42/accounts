from fastapi import FastAPI, File
import uvicorn
from typing import Annotated, List

from models.transaction import Transaction
from models.report import Report
from handlers.add_transactions import add_transactions
from handlers.make_report import make_report


app = FastAPI()

@app.post("/transactions")
async def handle_transactions(data: Annotated[bytes, File()]) -> List[Transaction]:
    return await add_transactions(data) 

@app.get("/report")
async def handle_get_report() -> Report:
    return await make_report()


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)     
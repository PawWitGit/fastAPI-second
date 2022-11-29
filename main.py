from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

@app.get("/items_not_int/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}
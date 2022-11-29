from fastapi import FastAPI
from enum import Enum

app = FastAPI()

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model name": model_name, "message": "Deep learning FTW!"}

    if model_name.value == "lenet":
        return {"model name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}


# @app.get("/users")
# async def read_users():
#     return ["Rick", "Morty"]
#
#
# @app.get("/users")
# async def read_users2():
#     return ["Bean", "Elfo"]

# @app.get("/users/me")
# async def read_user_me():
#     return {"user_id": "the current user"}
#
# @app.get("/users/{user_id}")
# async def read_user (user_id: int):
#     return {"user_id": user_id}


# @app.get("/items/{item_id}")
# async def read_item(item_id: int):
#     return {"item_id": item_id}
#
# @app.get("/items_not_int/{item_id}")
# async def read_item(item_id):
#     return {"item_id": item_id}

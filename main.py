import random

from fastapi import FastAPI

App = FastAPI()

# 127.0.0.1:8000/
@App.get("/")
async def root():
    return {"massage": "Hello World"}

# 127.0.0.1:8000/teste1
@App.get("/teste1")
async def funcaoteste():
    return {"teste": True, "num_aleatorio": random.randint(0, 2000 )}
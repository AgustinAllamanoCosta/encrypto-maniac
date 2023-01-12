import datetime

from fastapi import FastAPI

app = FastAPI()

@app.get("/healthCheck")
def read_root():
    return {"Time": datetime.datetime.now(), "Greeting": "Hello There"}

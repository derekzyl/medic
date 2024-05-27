from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.app import init_app

app, y = init_app()


app.mount("/static", StaticFiles(directory="static"), name="static")
# app.on_event("startup")

@app.get('/')
async def root():
    return {"message":"hello world"}
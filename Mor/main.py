from fastapi import FastAPI
from controller.controller import datalikeController
app= FastAPI()

app.include_router(datalikeController)
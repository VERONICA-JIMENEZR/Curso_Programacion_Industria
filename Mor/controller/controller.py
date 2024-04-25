from fastapi import APIRouter
from models.datalike import datalike
from service.datalikeService import datalikeService
from typing import List
from models.datalike_model import datalikeDTO

datalikeController= APIRouter()
service= datalikeService()

@datalikeController.get("/datalike")
def getdatalike():
    return service.getdatalike()

@datalikeController.post("/datalike/create")
def createdatalike(data: datalikeDTO):
    return service.createdatalike(data)

@datalikeController.put("/datalike/update/{id}")
def updatedatalike(id:int, data:datalikeDTO):
    return service.updatedatalike(id,data)

@datalikeController.delete("/datalike/{id}")
def deletedatalike(id: int):
    return service.deletedatalike(id)
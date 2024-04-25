from sqlalchemy import or_
from config.config import conn
from models.datalike import datalike
from models.datalike_model import datalikeDTO

class datalikeService():    
    def getdatalike(self):
        result=conn.execute(datalike.select())
        resultAsList=[r._asdict() for r in result]
        return resultAsList
    
    def createdatalike(self,data: datalikeDTO):
        return conn.execute(datalike.insert().values(data.__dict__))
    
    def updatedatalike(self,id:int,data:datalikeDTO):
        values= data.__dict__
        print(values)
        conn.execute(datalike.update().where(datalike.c.id == id).values(values))
        return values
    def deletedatalike(self,id:int):
        return conn.execute(datalike.delete().where(datalike.c.id == id))
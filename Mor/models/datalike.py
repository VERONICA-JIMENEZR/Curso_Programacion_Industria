from sqlalchemy import Table,Column
from sqlalchemy.sql.sqltypes import Integer,String
from config.config import engine,meta_data

datalike= Table("Datalike", meta_data, 
              Column("Id",Integer, primary_key=True),
              Column("Nombre",String(100), nullable=False),
              Column("Apellido",String(100), nullable=False),
              Column("Celular",String(20), nullable=False),
              Column("Edad",Integer, nullable=False),
              
              )

meta_data.create_all(engine)
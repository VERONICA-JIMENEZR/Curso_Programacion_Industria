from sqlalchemy import create_engine, MetaData
URL="postgresql://postgres:1234@localhost:5432/datalike"

engine= create_engine(URL)

conn=engine.connect()

meta_data=MetaData()
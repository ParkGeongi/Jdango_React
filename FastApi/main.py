
from fastapi import FastAPI
from app.models.user import User
from fastapi_sqlalchemy import DBSessionMiddleware, db


app = FastAPI()
USERNAME = 'root'
PASSWORD = 'root'
HOSTNAME = 'localhost'
PORT = '3360'
DBNAME = 'mydb'
MYSQL_URL = "mysql+pymysql://root:root@localhost:3306/mydb"
db_url = MYSQL_URL
app.add_middleware(DBSessionMiddleware, db_url=MYSQL_URL)

@app.get('/test')
async def test():
  query = db.session.query(User)
  return query.all()

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}




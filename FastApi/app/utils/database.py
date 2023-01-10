import pymysql
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from app.utils.env import DB_USER, DB_PASSWORD, DB_HOST, PORT, DB_NAME, DB_URL, CHARSET

Base = declarative_base()

engine = create_engine(DB_URL, echo=True)

pymysql.install_as_MySQLdb()
conn = pymysql.connect(host=DB_HOST, port=PORT, user=DB_USER, password=DB_PASSWORD, db=DB_NAME, charset=CHARSET)

SessionLocal = scoped_session(
    sessionmaker(autocommit = False, autoflush=False, bind=engine)
)
Base.query = SessionLocal.query_property()

def get_db():
    global db
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


'''
class engineconn(object):

    def __init__(self):
        self.engine = create_engine(f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{PORT}/{DB_NAME}?charset=utf8mb4",future=True)
#172.17.0.1 -> docker host host.docker.internal
    def sessionmaker(self):
        Session = sessionmaker(bind=self.engine)
        session = Session()
        session.close()
        return session

    def connection(self):
        conn = self.engine.connect()
        conn.close()
        return conn
'''



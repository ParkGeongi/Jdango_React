from pydantic import BaseModel, BaseConfig
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.future import create_engine
from sqlalchemy.orm import Session, relationship, declarative_base, sessionmaker

Base = declarative_base()
class User(Base):
    __tablename__ = 'users'
    users_id = Column(primary_key=True)
    user_email = Column(String(20), nullable=False)
    password = Column(String(20), nullable=False)
    user_name = Column(String(20), nullable=False)
    phone = Column(String(20))
    birth = Column(String(20))
    address = Column(String(20))
    job = Column(String(20))
    user_interests = Column(String(20))
    token = Column(String(20))

    class Config:
        BaseConfig.arbitrary_types_allowed = True
        allow_population_by_field_name = True


class engineconn:

    def __init__(self):
        self.engine = create_engine("mysql+pymysql://root:root@host.docker.internal:3306/mydb",future=True)

    def sessionmaker(self):
        Session = sessionmaker(bind=self.engine)
        session = Session()
        session.close()
        return session

    def connection(self):
        conn = self.engine.connect()
        conn.close()
        return conn




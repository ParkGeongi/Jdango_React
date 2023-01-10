from pydantic import BaseModel, BaseConfig
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.future import create_engine
from sqlalchemy.orm import Session, relationship, sessionmaker
from app.utils.database import Base
class Article(Base):
    __tablename__ = 'posts'
    post_id = Column(primary_key=True)
    title = Column(String(100))
    content = Column(String(1000))
    create_at = Column(String(30))
    updated_at = Column(String(30))

    class Config:
        BaseConfig.arbitrary_types_allowed = True
        allow_population_by_field_name = True
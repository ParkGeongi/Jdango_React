from pydantic import BaseModel, BaseConfig
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.future import create_engine
from sqlalchemy.orm import Session, relationship, sessionmaker
from sqlalchemy_utils import UUIDType
from app.models.mixins import TimstampMixin
from app.utils.database import engine, Base


class Article(Base, TimstampMixin):
    __tablename__ = 'articles'
    art_seq = Column(Integer,primary_key=True, autoincrement=True)
    title = Column(String(100))
    content = Column(String(1000))
    users_id = Column(UUIDType(binary=False), ForeignKey('users.user_id'), nullable=True)
    user = relationship('User',back_populates='articles')

    class Config:
        BaseConfig.arbitrary_types_allowed = True
        allow_population_by_field_name = True
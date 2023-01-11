from uuid import uuid4

from pydantic import BaseModel, BaseConfig
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String

from sqlalchemy.orm import Session, relationship, sessionmaker

from app.models.mixins import TimstampMixin
from app.utils.database import engine, Base
from sqlalchemy_utils import UUIDType


class User(Base,TimstampMixin):
    __tablename__ = 'users'
    user_id = Column(UUIDType(binary=False), primary_key=True, default=uuid4)
    user_email = Column(String(20), nullable=False)
    password = Column(String(20), nullable=False)
    user_name = Column(String(20), nullable=False)
    phone = Column(String(20))
    birth = Column(String(20))
    address = Column(String(20))
    job = Column(String(20))
    user_interests = Column(String(20))
    token = Column(String(20))
    articles = relationship('Article', back_populates='user')

    class Config:
        BaseConfig.arbitrary_types_allowed = True
        allow_population_by_field_name = True







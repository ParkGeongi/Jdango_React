from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.models.user import engineconn, User
from app.repositories.user import find_users
router = APIRouter()

engine = engineconn()
session = engine.sessionmaker()
conn = engine.connection()

@router.get("/")
async def get_all_items():
    return session.query(User).all()


from fastapi import APIRouter, Depends
import app.repositories.user as dao
from sqlalchemy.orm import Session

from app.schemas.user import User
from app.utils.database import get_db

router = APIRouter()


## C
@router.post("/")
async  def join(item: User, db: Session = Depends(get_db)):
    user_dict = item.dict()
    print((f"SignUp Inform : {user_dict}"))
    dao.join(item=item,db=db)
    return {"data":"sucess"}

@router.post("/{id}")
async def login(id:str,item:User, db: Session = Depends(get_db)):
    dao.login(id, item, db)
    return {"data": "success"}

@router.put("/{id}")
async def update(id:str,item: User, db: Session = Depends(get_db)):
    dao.update(id=id,item=item,db=db)
    return {"data":"sucess"}

@router.delete("/{id}")
async def delete(id:str,user: User, db: Session = Depends(get_db)):
    dao.delte(id=id,item=user,db=db)
    return {"data":"sucess"}

## Q
@router.get("/{page}")
async def get_users(page, db: Session = Depends(get_db)):
    ls = dao.find_users(page,db)
    return {"data": ls}

@router.get("/email/{id}")
async def get_user(id : str,db: Session = Depends(get_db)):
    dao.find_user(id=id,db=db)
    return {"data": "sucess"}

@router.get("/job/{search}/{page}")
async def get_users_by_job(search: str, page: int, db: Session = Depends(get_db)):
    dao.find_users_by_job(search,page,db)
    return {"data":"sucess"}

'''
@router.get("/2")
async def get_users_legacy():
    return dao.find_users_legacy()
    
@router.get("/")
async def get_users():
    return dao.find_users()

'''
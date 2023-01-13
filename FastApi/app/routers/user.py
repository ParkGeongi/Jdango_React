from fastapi import APIRouter, Depends
import app.repositories.user as dao
from sqlalchemy.orm import Session

from app.admin.utils import current_time
from app.models.user import User
from app.schemas.user import UserDTO
from app.database import get_db

router = APIRouter()


## C
@router.post("/join")
async def join(user: UserDTO, db: Session = Depends(get_db)):
    print(f" 회원가입에 진입한 시간: {current_time()} ")
    print(f"SignUp Inform : {user}")
    result = dao.join(user, db)
    if result =="":
        result = "failure"
    return {"data": result}

@router.post("/login")
async def login(user:UserDTO ,db: Session = Depends(get_db)):

    return_user = dao.login(user, db)
    print(f"로그인 정보 : {return_user}")
    return {"data": return_user}

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
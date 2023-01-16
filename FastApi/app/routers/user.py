from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse

from app.admin.security import get_hashed_password, generate_token
from app.admin.utils import current_time
from app.cruds.user import UserCrud
from app.models.user import User
from app.schemas.user import UserDTO
from app.database import get_db

router = APIRouter()


## C
@router.post("/register",status_code=201)
async def register_user(dto: UserDTO, db: Session = Depends(get_db)):
    print(f" 회원가입에 진입한 시간: {current_time()} ")
    print(f"SignUp Inform : {dto}")
    user_crud = UserCrud(db)
    userid = user_crud.find_userid_by_email(dto)
    print(userid)
    if userid =="":
        print(f'해시전 비번 : {dto.password}')
        dto.password = get_hashed_password(dto.password)
        print(f"해시후 비번 : {dto.password}")
        result = {'data' :user_crud.add_user(request_user=dto)}
    else:
        result = JSONResponse(status_code = 400, content=dict(msg='이메일이 이미 존재합니다'))

    return result

@router.post("/login", status_code=200)
async def login(dto:UserDTO ,db: Session = Depends(get_db)):
    user_crud = UserCrud(db)
    userid = user_crud.find_userid_by_email(request_user=dto)
    dto.userid= userid
    print(f'로그인 보내기 전에 확인 ID{dto.userid}, password {dto.password}')
    if userid != '':
        login_user = user_crud.login(request_user=dto)
        if login_user is not None:
            print(f'로그인 성공 정보: \n{login_user}')
            new_token = generate_token(login_user.email)
            print(new_token)
            login_user.token = new_token
            result = {'data':login_user}
        else:
            print('로그인 실패')
            result = JSONResponse(status_code=400,content = dict(msg="비밀번호 일치하지 않습니다."))
    else:
        result = JSONResponse(status_code=400, content=dict(msg="이메일 주소가 일치하지 않습니다."))

    return result

@router.put("/{id}")
async def update(id:str,item: User, db: Session = Depends(get_db)):
    UserCrud(db).update(id=id,item=item)
    return {"data":"sucess"}

@router.delete("/{id}")
async def delete(id:str,user: User, db: Session = Depends(get_db)):
    UserCrud(db).delte(id=id,item=user,db=db)
    return {"data":"sucess"}

## Q
@router.get("/{page}")
async def get_users(page, db: Session = Depends(get_db)):
    ls = UserCrud(db).find_users(page,db)
    return {"data": ls}

@router.get("/email/{id}")
async def get_user(id : str,db: Session = Depends(get_db)):
    UserCrud(db).find_user(id=id,db=db)
    return {"data": "sucess"}

@router.get("/job/{search}/{page}")
async def get_users_by_job(search: str, page: int, db: Session = Depends(get_db)):
    UserCrud(db).find_users_by_job(search,page,db)
    return {"data":"sucess"}

'''
@router.get("/2")
async def get_users_legacy():
    return dao.find_users_legacy()
    
@router.get("/")
async def get_users():
    return dao.find_users()

'''
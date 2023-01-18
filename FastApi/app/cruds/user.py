from abc import ABC
from typing import List

from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.admin.security import verify_password
from app.bases.user import UserBase
from app.models.user import User
from app.schemas.user import UserDTO
from starlette.responses import JSONResponse


class UserCrud(UserBase, ABC):
    def __init__(self, db:Session):
        self.db : Session = db

    def add_user(self, request_user: UserDTO) -> str:
        self.db.add(User(**request_user.dict()))
        self.db.commit()
        return "success"

    def login(self, request_user: UserDTO):
        target = self.find_user_by_id(request_user)
        verified = verify_password(plain_password=request_user.password,
                                   hashed_password=target.password)
        print(f"검증결과 : {verified}")
        if verified:
            return target
        else:
            return None


    def update_user(self,email:str, request_user: UserDTO):
        user = User(**request_user.dict())
        email = user.email
        update_query = self.db.query(User).filter(User.email == email)
        update = update_query.first()
        if not update:
            return 'fail'
        update_data = request_user.dict(exclude_unset=True)
        del(update_data['email'])
        update_query.filter(User.email == email).update(update_data,synchronize_session=False)
        self.db.commit()
        return 'success'
    def delete_user(self, email: str, request_user: UserDTO) -> str:
        user = User(**request_user.dict())
        email = user.email
        delete_email_query = self.db.query(User).filter(User.email == email)
        delete_email = delete_email_query.first()
        if not delete_email:
            return 'fail'
        delete_email_query.delete(synchronize_session=False)
        self.db.commit()
        return 'success'

    def find_all_user(self, page: int) -> List[User]:
        print(f"page number is {page}")
        return self.db.query(User).all()

    def find_user_by_id(self, request_user: UserDTO) -> UserDTO:
        user = User(**request_user.dict())
        return self.db.query(User).filter(User.userid == user.userid).first()

    def find_userid_by_email(self, request_user: UserDTO) -> str:
        user = User(**request_user.dict())
        db_user = self.db.query(User).filter(User.email == user.email).first()
        if db_user is not None:
            return db_user.userid
        else:
            return ""

    def find_users_by_job(self, request_user: UserDTO) -> list:
        user = User(**request_user.dict())
        return self.db.query(User).filter(User.job == user.job).all()




'''
def find_users_legacy():
    conn = pymysql.connect(host=DB_HOST, port=PORT, user=DB_USER, password=DB_PASSWORD, db=DB_NAME, charset='utf8')
    cursor = conn.cursor()  # MySQL에 접속
    sql = "select * from users"  # 적용할 MySQL 명령어를 만들어서 sql 객체에 할당하면 됨
    cursor.execute(sql)
    result = cursor.fetchall()
    return result
    
def login():
    user = User(**request_user.dict())
        db_user = self.db.scalars(select(User).where(User.user_email == user.user_email)).first()
        print(f" dbUser {db_user}")
        if db_user is not None:
            if db_user.password == user.password:
                return db_user
            else:
                return 'password fail'
        else:
            print("해당 이메일이 없습니다.")
            return "email failure"    
'''

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user import UserDTO


def find_users(page,db: Session):
    print(f"page number is {page}")
    return db.query(UserDTO).all()



def join(userDTO: UserDTO, db: Session)->str:
    user = User(**userDTO.dict())
    db.add(user)
    db.commit()
    return "success"


def login(userDTO: UserDTO, db: Session):
    user = User(**userDTO.dict())
    #db_user = user.select().where(user.colums.useremail == 'lgv@naver.com')
    # db.query(db_user.exists())
    db_user = db.scalars(select(User).where(User.user_email==user.user_email)).first()
    print(f" dbUser {db_user}")
    if db_user is not None:
        if db_user.password == user.password:
            return db_user
    else:
        print("해당 이메일이 없습니다.")
        return "failure"


def update(id, item, db):
    return None


def delte(id, item, db):
    return None


def find_user(id, db):
    return None


def find_users_by_job(search, page, db):
    return None
'''
def find_users_legacy():
    conn = pymysql.connect(host=DB_HOST, port=PORT, user=DB_USER, password=DB_PASSWORD, db=DB_NAME, charset='utf8')
    cursor = conn.cursor()  # MySQL에 접속
    sql = "select * from users"  # 적용할 MySQL 명령어를 만들어서 sql 객체에 할당하면 됨
    cursor.execute(sql)
    result = cursor.fetchall()
    return result
'''

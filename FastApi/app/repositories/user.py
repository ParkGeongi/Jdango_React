import pymysql
from sqlalchemy.orm import Session

from app.models.user import User
from app.utils.env import DB_USER, DB_PASSWORD, DB_HOST, PORT, DB_NAME



def find_users_legacy():
    conn = pymysql.connect(host=DB_HOST, port=PORT, user=DB_USER, password=DB_PASSWORD, db=DB_NAME, charset='utf8')
    cursor = conn.cursor()  # MySQL에 접속
    sql = "select * from users"  # 적용할 MySQL 명령어를 만들어서 sql 객체에 할당하면 됨
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

def find_users(page,db: Session):
    print(f"page number is {page}")
    return db.query(User).all()



def join(item, db):
    return None


def login(id, item, db):
    return None


def update(id, item, db):
    return None


def delte(id, item, db):
    return None


def find_user(id, db):
    return None


def find_users_by_job(search, page, db):
    return None
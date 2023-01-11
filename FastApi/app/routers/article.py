from fastapi import APIRouter, Depends
import app.repositories.articles as dao
from sqlalchemy.orm import Session

from app.models.articles import Article
from app.utils.database import get_db

router = APIRouter()


@router.post("/")
async def wrtie(item: Article, db: Session = Depends(get_db)):
    article_dict = item.dict()
    print((f"SignUp Inform : {article_dict}"))
    dao.join(item=item,db=db)
    return {"data":"sucess"}


@router.put("/{seq}")
async def update(seq:str,item: Article, db: Session = Depends(get_db)):
    dao.update(id=seq,item=item,db=db)
    return {"data":"sucess"}

@router.delete("/{seq}")
async def delete(seq:str,user: Article, db: Session = Depends(get_db)):
    dao.delte(id=seq,item=user,db=db)
    return {"data":"sucess"}

## Q
@router.get("/{page}")
async def get_articles(page, db: Session = Depends(get_db)):
    ls = dao.find_articles(page,db)
    return {"data": ls}

@router.get("/email/{seq}")
async def get_article(seq : str,db: Session = Depends(get_db)):
    dao.find_article(id=seq,db=db)
    return {"data": "sucess"}

@router.get("/job/{search}/{no}")
async def get_article_by_title(search: str, page: int, db: Session = Depends(get_db)):
    dao.find_article_by_title(search,page,db)
    return {"data":"sucess"}

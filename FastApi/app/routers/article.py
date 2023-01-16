from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from app.cruds.article import ArticleCrud
from app.schemas.article import ArticleDTO
from app.database import get_db

router = APIRouter()


@router.post("/write")
async def wrtie(dto: ArticleDTO, db: Session = Depends(get_db)):
    article_crud = ArticleCrud(db)
    d = article_crud.add_article(dto)
    if d == 'success':
        result = {'data': d}
    else:
        result = {'data':'fail'}
    return result


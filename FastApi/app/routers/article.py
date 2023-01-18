from fastapi import APIRouter, Depends
from starlette.responses import JSONResponse

from sqlalchemy.orm import Session

from app.admin.utils import current_time
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

@router.put("/update/{userid}")
async def update(userid:str,dto:ArticleDTO ,db: Session = Depends(get_db)):
    article_crud = ArticleCrud(db)
    print(f" 업데이트에 진입한 시간: {current_time()} ")
    result = article_crud.update_article_by_userid(request_article=dto)
    if result == 'success':
        return {'data', f'update {userid} success'}

    return JSONResponse(status_code=404, content=dict(msg="해당 아이디가 없습니다."))

@router.delete("/delete/{title}")
async def delete(title:str,dto:ArticleDTO ,db: Session = Depends(get_db)):
    article_crud = ArticleCrud(db)
    print(f" 삭제에 진입한 시간: {current_time()} ")
    result = article_crud.delete_article_by_title(request_article=dto)
    if result =='success':
        return {'data',f'delete {title} success'}
    else:
        return JSONResponse(status_code=404, content=dict(msg="타이틀이 없습니다."))

@router.get("/{page}")
async def get_articles(page:int,db: Session = Depends(get_db)):
    article_crud = ArticleCrud(db)
    result = article_crud.find_all_articles(page)
    return result## Q

@router.get("/find/userid/{page}")
async def get_articles_by_userid(page:int,dto:ArticleDTO,db: Session = Depends(get_db)):
    article_crud = ArticleCrud(db)
    result = article_crud.find_articles_by_userid(page,request_article=dto)
    return result

from abc import ABC

from app.bases.article import ArticleBase
from app.models.article import Article

from sqlalchemy.orm import Session

from app.schemas.article import ArticleDTO


class ArticleCrud(ArticleBase,ABC):

    def __init__(self,db:Session):
        self.db : Session = db
    def add_article(self, request_article: ArticleDTO) -> str:
        self.db.add(Article(**request_article.dict()))
        self.db.commit()
        return "success"




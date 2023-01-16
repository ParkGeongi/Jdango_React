from abc import ABCMeta,abstractmethod

from app.schemas.article import ArticleDTO


class ArticleBase(metaclass=ABCMeta):
    @abstractmethod
    def add_article(self, request_article: ArticleDTO)->str:
        pass


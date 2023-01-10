from typing import List

from pydantic import BaseModel


class Article(BaseModel):
    post_id : int
    title : str
    content : str
    create_at : str
    updated_at : str


    class Config:
        orm_mode = True
from datetime import datetime
from typing import List

from pydantic import BaseModel



class TimstampMixin(BaseModel):
    create_at : datetime
    updated_at : datetime


    class Config:
        orm_mode = True
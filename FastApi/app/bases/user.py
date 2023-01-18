from abc import abstractmethod,ABCMeta
from typing import List
from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user import UserDTO


class UserBase(metaclass=ABCMeta):

    @abstractmethod
    def add_user(self, request_user: UserDTO) -> str: pass

    @abstractmethod
    def login(self, request_user: UserDTO) -> User: pass


    @abstractmethod
    def update_user(self,email:str, request_user: UserDTO) -> str: pass


    @abstractmethod
    def delete_user(self,email:str, request_user: UserDTO) -> str: pass


    @abstractmethod
    def find_all_user(self, page: int) -> List[User]: pass

    @abstractmethod
    def find_user_by_id(self, page: int) -> UserDTO: pass

    @abstractmethod
    def find_userid_by_email(self, request_user: UserDTO) -> str: pass
    @abstractmethod
    def find_users_by_job(self, request_user: UserDTO) -> UserDTO:pass

from typing import List
from core.entities.user_entity import UserEntity

class UserRepository:

    def get_all(self) -> List[UserEntity]:
        raise NotImplementedError
    
    def get_by_id(self, id: int) -> UserEntity:
        raise NotImplementedError

    def create(self, user: UserEntity) -> None:
        raise NotImplementedError
from typing import List
from core.interfaces.user_repository import UserRepository
from core.entities.user_entity import UserEntity

class UserService:
    def __init__(self, repository: UserRepository) -> None:
        self.repository = repository

    def list_users(self) -> List[UserEntity]:
        return self.repository.get_all()

    def get_user_by_id(self, id:int) -> UserEntity:
        return self.repository.get_by_id(id)
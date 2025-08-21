from abc import ABC, abstractmethod
from api.core.entities.user_entity import UserEntity


class UserRepositoryInterface(ABC):
    @abstractmethod
    def get_all(self) -> list[UserEntity]:
        pass
    
    @abstractmethod
    def create(self, user: UserEntity) -> UserEntity:
        pass



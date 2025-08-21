from api.core.interfaces.user_repository import UserRepositoryInterface
from api.core.entities.user_entity import UserEntity

class UserUseCase:
    def __init__(self, repository: UserRepositoryInterface):
            self.repository = repository 

    def list_users(self):
        return self.repository.get_all()
    
    def create(self, first_name: str, last_name: str, email: str, password: str):
        new_user = UserEntity(id=None, first_name=first_name, last_name=last_name, email=email, password=password)
        return self.repository.create(new_user)
from typing import List
from api.core.entities.user_entity import UserEntity
from api.core.interfaces.user_repository import UserRepositoryInterface
from api.infra.db.models import User

class UserRepository(UserRepositoryInterface):
    
    def get_all(self) -> List[UserEntity]:
        users = User.objects.all()
        return [
            UserEntity(
                id=str(user.id),
                first_name=user.first_name,
                last_name=user.last_name,
                email=user.email,
                password=user.password
            )
            for user in users
        ]

    def create(self, user: UserEntity) -> UserEntity:
        new_user = User.objects.create(
            first_name=user.first_name,
            last_name=user.last_name,
            email=user.email,
            password = user.password
        )
        new_user.save()

        return UserEntity(
            id=new_user.id,
            first_name=new_user.first_name,
            last_name=new_user.last_name,
            email=new_user.email,
            password=new_user.password
        )
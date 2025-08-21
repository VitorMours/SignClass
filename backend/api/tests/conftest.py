from api.core.entities.user_entity import UserEntity
import pytest
import uuid

@pytest.fixture
def user_id():
    """Cria e retorna um novo UUID para os testes."""
    return uuid.uuid4()

@pytest.fixture
def default_user():
    id = uuid.uuid4()
    user = UserEntity(id,"Alice","Doe","alice.doe@email.com","password_123!")
    return user
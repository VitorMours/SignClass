import uuid
import pytest
from core.entities.user_entity import UserEntity

class TestUserEntity:


    def test_if_user_entity_tests_are_running(self) -> None:
        assert True

    def test_creating_user_with_standard_parameters(self, user_id) -> None:
        id = uuid.uuid4()
        user = UserEntity(user_id,"Lucas","Moura","lucas.moura@email.com","32322916aA!")
        assert user.id == user_id
        assert user.first_name == "Lucas"
        assert user.last_name == "Moura"
        assert user.email == "lucas.moura@email.com"
        assert user.password == "32322916aA!"
    
    def test_error_creating_user_with_wrong_type_in_first_name(self, user_id) -> None:  
        with pytest.raises(TypeError) as exec_info:
            user = UserEntity(user_id, 123123, "Moura", "lucas.moura@email.com", "32322916aA!")

        assert "O primeiro nome deve ser uma string." in str(exec_info.value)

    
    def test_error_creating_user_with_wrong_type_in_last_name(self, user_id) -> None:  
        with pytest.raises(TypeError) as exec_info:
            user = UserEntity(user_id, "Lucas", 123123, "lucas.moura@email.com", "32322916aA!")

        assert "O ultimo nome deve ser uma string." in str(exec_info.value)
        
    def test_error_creating_user_with_wrong_type_in_email(self, user_id) -> None:  
        with pytest.raises(TypeError) as exec_info:
            user = UserEntity(user_id, "Lucas", "Moura", 123123, "32322916aA!")

        assert "O email deve ser uma string." in str(exec_info.value)

    def test_error_creating_user_with_wrong_type_in_password(self, user_id) -> None:  
        with pytest.raises(TypeError) as exec_info:
            user = UserEntity(user_id, "Lucas", "Moura", "lucas.moura@email.com", 123123)

        assert "A senha deve ser uma string." in str(exec_info.value)

    def test_get_user_data_after_creation(self, default_user) -> None:
        assert default_user.first_name == "Alice"
        assert default_user.last_name == "Doe"
        assert default_user.email == "alice.doe@email.com"
        assert default_user.password == "password_123!"



    def test_set_user_data_after_creation(self, default_user) -> None:
        default_user.first_name = "Bob"
        default_user.last_name = "John"
        default_user.email = "john.john@email.com"
        default_user.password = "123-password"
        
        
        assert default_user.first_name == "Bob"
        assert default_user.last_name == "John"
        assert default_user.email == "john.john@email.com"
        assert default_user.password == "123-password"



    # TODO: Implementar o os testes que tentam atribuir um valor do tipo primitivo errado, e levantar um erro do tipo TypeError.
    # esse teste deve ser feito para cada um dos campos

    # Essa linha abaixo é somente para o pytest por hora ignorar o test, n executando ele, mas deixar o mesmo existir sem levantar erros
    @pytest.mark.skip(reason="TODO Implementar esse teste")
    def test_set_wrong_type_user_data_after_creation(self, default_user) -> None:
        assert default_user.last_name == "Doe"
        assert default_user.email == "alice.doe@email.com"
        assert default_user.password == "password_123!"
        assert default_user.first_name == 123



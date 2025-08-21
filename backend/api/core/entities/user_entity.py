from dataclasses import dataclass, field
import uuid
from typing import Any

@dataclass
class UserEntity:
    id: uuid.UUID
    _first_name: str = field(init=False, repr=False)
    _last_name: str = field(init=False, repr=False)
    _email: str = field(init=False, repr=False)
    _password: str = field(init=False, repr=False)

    def __init__(self, id, first_name, last_name, email, password):
        # Assigns values to the hidden attributes, which calls the setters
        # for validation.
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    @classmethod
    def _validate_as_string(cls, data: Any) -> bool:
        """Validates if the given data is a string."""
        return isinstance(data, str)

    @property
    def id(self) -> uuid.UUID:
        return self._id

    @id.setter
    def id(self, value: Any):
        if not isinstance(value, uuid.UUID):
            raise TypeError("The ID must be a UUID object.")
        self._id = value

    @property
    def first_name(self) -> str:
        return self._first_name

    @first_name.setter
    def first_name(self, value: Any):
        if not UserEntity._validate_as_string(value):
            raise TypeError("O primeiro nome deve ser uma string.")
        self._first_name = value

    @property
    def last_name(self) -> str:
        return self._last_name

    @last_name.setter
    def last_name(self, value: Any):
        if not UserEntity._validate_as_string(value):
            raise TypeError("O ultimo nome deve ser uma string.")
        self._last_name = value

    @property
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, value: Any):
        if not UserEntity._validate_as_string(value):
            raise TypeError("O email deve ser uma string.")
        self._email = value

    @property
    def password(self) -> str:
        return self._password

    @password.setter
    def password(self, value: Any):
        if not UserEntity._validate_as_string(value):
            raise TypeError("A senha deve ser uma string.")
        self._password = value
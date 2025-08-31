from dataclasses import dataclass, field
import uuid


@dataclass(frozen=True) 
class UserEntity:
    id: uuid.uuid4
    first_name: str
    last_name: str
    email: str
    password: str
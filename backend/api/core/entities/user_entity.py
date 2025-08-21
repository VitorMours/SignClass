from dataclasses import dataclass
import uuid

@dataclass 
class UserEntity:
    id : uuid.uuid4
    first_name : str
    last_name : str
    email : str
    password : str
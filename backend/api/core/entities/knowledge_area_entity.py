from dataclasses import dataclass, fields 


@dataclass(frozen=True)
class KnowledgeAreaEntity:
    name: str 
    content: str 
    area: str 
    videos_quantity: int

from abc import ABC, abstractmethod
from core.entities.knowledge_area_entity import KnowledgeAreaEntity


class KnowledgeAreaRepositoryInterface(ABC):

    @abstractmethod
    def get_area_videos(self) -> None:
        raise NotImplementedError
    
    @abstractmethod
    def get_area_students(self) -> None:
        raise NotImplementedError

from abc import ABC, abstractmethod
from models.document import Document


class Parser(ABC):
    """Abstract base class for all document methods"""

    @abstractmethod
    def parse(self, file_path: str) -> Document: ...

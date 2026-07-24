from abc import ABC, abstractmethod
from models.document import Document
from models.chunk import Chunk


class Chunker(ABC):
    """Abstract base class for all chunking methods"""

    @abstractmethod
    def chunk(self, document: Document) -> list[Chunk]:
        ...
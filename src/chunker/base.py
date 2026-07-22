from abc import ABC, abstractmethod


class Chunker(ABC):
    """Abstract base class for all chunking methods"""

    @abstractmethod
    def chunk(self, text: str) -> list[str]: ...


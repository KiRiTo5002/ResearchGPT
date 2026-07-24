from abc import ABC, abstractmethod

from models.chunk import Chunk
from models.embedded_chunk import EmbeddedChunk


class VectorStore(ABC):
    @abstractmethod
    def store(
        self,
        embedded_chunks: list[EmbeddedChunk],
    ) -> None: ...

    @abstractmethod
    def search(
        self,
        query_embedding: list[float],
        limit: int = 5,
    ) -> list[Chunk]: ...

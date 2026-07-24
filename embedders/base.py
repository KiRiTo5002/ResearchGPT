from abc import ABC, abstractmethod 

class Embedder(ABC):
    
    @abstractmethod
    def embed(
        self,
        texts: list[str],
    ) -> list[list[float]]:
        ...

    @property
    @abstractmethod
    def embedding_dimension(self) -> int:
        ...
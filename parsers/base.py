from abc import ABC, abstractmethod

class Parser(ABC):
    """Abstract base class for all document methods"""
    @abstractmethod
    def parse(self, file_path: str) -> str:
        pass

    

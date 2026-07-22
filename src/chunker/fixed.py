from chunker.base import Chunker


class FixedChunker(Chunker):
    def __init__(self, chunk_size: int, chunk_overlap: int):

        if chunk_size <= 0:
            raise ValueError("Chunk size must be positive.")

        if chunk_overlap < 0:
            raise ValueError("Chunk overlap cannot be negative.")

        if chunk_overlap >= chunk_size:
            raise ValueError("Chunk overlap must be smaller than chunk size.")

        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

    def chunk(self, text: str) -> list[str]:

        start = 0
        stride = self.chunk_size - self.chunk_overlap
        chunks = []

        while start < len(text):
            chunk = text[start : start + self.chunk_size]
            chunks.append(chunk)
            start += stride

        return chunks

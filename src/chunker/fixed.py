from chunker.base import Chunker
from models.document import Document
from models.chunk import Chunk


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

    def chunk(self, document: Document) -> list[Chunk]:

        stride = self.chunk_size - self.chunk_overlap

        chunks: list[Chunk] = []

        chunk_index = 1

        for page in document.pages:
            start = 0

            while start < len(page.text):
                chunk_text = page.text[start : start + self.chunk_size]

                chunk = Chunk(
                    chunk_id=str(chunk_index)+"_"+document.document_id,
                    document_id=document.document_id,
                    page_number=page.number,
                    chunk_text=chunk_text,
                )

                chunks.append(chunk)

                chunk_index += 1
                start += stride

        return chunks

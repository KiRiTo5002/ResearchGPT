from models.chunk import Chunk
from models.embedded_chunk import EmbeddedChunk


class EmbeddedChunkAssembler:
    def assemble(
        self, chunks: list[Chunk], embeddings: list[list[float]]
    ) -> list[EmbeddedChunk]:

        if len(chunks) != len(embeddings):
            raise ValueError("Invalid Embedding length for the Chunk")
        embedded_chunks = []
        for chunk, embedding in zip(chunks, embeddings):
            embedded_chunk = EmbeddedChunk(chunk=chunk, embedding=embedding)
            embedded_chunks.append(embedded_chunk)
        return embedded_chunks

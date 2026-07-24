from models.chunk import Chunk
from retrievers.base import Retriever

from embedders.base import Embedder
from vectorstores.base import VectorStore


class VectorRetriever(Retriever):
    def __init__(
        self,
        embedder: Embedder,
        vector_store: VectorStore,
    ):
        self.embedder = embedder
        self.vector_store = vector_store

    def retrieve(
        self,
        query: str,
        limit: int = 5,
    ) -> list[Chunk]:

        query_embedding = self.embedder.embed([query])[0]

        return self.vector_store.search(
            query_embedding=query_embedding,
            limit=limit,
        )

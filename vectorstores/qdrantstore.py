from models.embedded_chunk import EmbeddedChunk
from vectorstores.base import VectorStore
from qdrant_client import QdrantClient, models


class QdrantStore(VectorStore):
    def __init__(
        self,
        qdrant_url: str,
        qdrant_api_key: str,
        collection_name: str,
        vector_size: int,
    ):

        self.collection_name = collection_name
        self.vector_size = vector_size
        self.client = QdrantClient(
            url=qdrant_url,
            api_key=qdrant_api_key,
        )

    def _ensure_collection_exists(self) -> None:

        if not self.client.collection_exists(collection_name=self.collection_name):
            self.client.create_collection(
                collection_name=self.collection_name,
                vectors_config=models.VectorParams(
                    size=self.vector_size, distance=models.Distance.COSINE
                ),
            )

    def store(self, embedded_chunks: list[EmbeddedChunk]) -> None:

        self._ensure_collection_exists()
        points = []
        for embedded_chunk in embedded_chunks:
            point = models.PointStruct(
                id=embedded_chunk.chunk.chunk_id,
                vector=embedded_chunk.embedding,
                payload=embedded_chunk.chunk.model_dump(),
            )
            points.append(point)

        self.client.upsert(collection_name=self.collection_name, points=points)

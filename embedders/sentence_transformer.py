from sentence_transformers import SentenceTransformer
from typing import cast
from embedders.base import Embedder


class SentenceTransformerEmbedder(Embedder):

    def __init__(self, model_name: str):

        self.model = SentenceTransformer(model_name)

    def embed(
        self,
        texts: list[str],
    ) -> list[list[float]]:

        embeddings = self.model.encode(texts)

        return embeddings.tolist()
    
    @property
    def embedding_dimension(self) -> int:

        dimension = self.model.get_embedding_dimension()

        if dimension is None:
            raise RuntimeError("Embedding model does not expose its embedding dimension.")

        return dimension
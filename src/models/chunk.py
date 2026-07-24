from pydantic import BaseModel


class Chunk(BaseModel):
    """model for chunk returned by the chunker"""

    chunk_id: str
    document_id: str
    chunk_text: str
    page_number: int

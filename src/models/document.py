from pydantic import BaseModel
from models.page import Page


class Document(BaseModel):
    """model for Document returned by the parser"""

    document_name: str
    document_id: str
    document_type: str
    pages: list[Page]   

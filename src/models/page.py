from pydantic import BaseModel

class Page(BaseModel):

    number : int
    text : str 
    
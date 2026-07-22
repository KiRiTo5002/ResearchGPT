from parsers.pdf import PDFParser
from parsers.base import Parser


class ParserFactory:
    @staticmethod
    def create(file_path: str) -> Parser:

        normalised_path = file_path.lower()

        if normalised_path.endswith(".pdf"):
            parser = PDFParser()

        else:
            raise ValueError("Unsupported File extention")

        return parser

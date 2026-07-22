import pymupdf
from parsers.base import Parser


class PDFParser(Parser):
    def parse(self, file_path: str) -> str:
        with pymupdf.open(file_path) as document:
            if not document:
                raise ValueError("Source Document not found")
            page_text = []
            for page in document:
                text = page.get_text()
                if text:
                    page_text.append(text)
        return "\n\n".join(page_text)

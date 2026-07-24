import secrets
from pathlib import Path
from typing import cast

import pymupdf

from parsers.base import Parser
from models.document import Document
from models.page import Page


class PDFParser(Parser):
    """Parser for PDF documents."""

    def parse(self, file_path: str) -> Document:

        pages: list[Page] = []

        with pymupdf.open(file_path) as pdf:

            for page_number in range(pdf.page_count):

                pdf_page = pdf.load_page(page_number)

                text = cast(str, pdf_page.get_text("text"))

                page = Page(
                    number=page_number + 1,
                    text=text,
                )

                pages.append(page)

        document = Document(
            document_id=secrets.token_hex(20),
            document_name=Path(file_path).name,
            document_type=Path(file_path).suffix,
            pages=pages,
        )

        return document
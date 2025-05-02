from typing import Annotated
from pymupdf import Document, open, Page

from fastapi import Depends

from app.repository.file import FileRepository


class PDFParserService:
    def __init__(
        self,
        repository: Annotated[FileRepository, Depends()],
    ):
        self.repository = repository

    async def retrieve_images(self, filename: str):
        filepath = await self.repository.get_path(filename=filename)
        doc = open(filepath)
        for page in doc.pages():
            if not page.get_text():
                match page.get_images():
                    case [(xref, *_)]:
                        print(doc.extract_image(xref))
        return filepath

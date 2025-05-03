from typing import Annotated
from pymupdf import Document, open, Page
from mistralai import Mistral
from app.integrations.ocr import get_ai_model

from fastapi import Depends

from app.repository.file import FileRepository


class PDFParserService:
    def __init__(
        self,
        repository: Annotated[FileRepository, Depends(get_ai_model)],
        parser: Annotated[Mistral, Depends()]
    ):
        self.repository = repository
        self.parser = parser

    async def retrieve_images(self, filename: str):
        filepath = await self.repository.get_path(filename=filename)
        doc = open(filepath)
        for page in doc.pages():
            if not page.get_text():
                match page.get_images():
                    case [(xref, *_)]:
                        print(doc.extract_image(xref))
        return filepath

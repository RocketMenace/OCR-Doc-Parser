from typing import Annotated
from fastapi import Depends
from mistralai import Mistral
from app.integrations.ocr import get_ai_model
import pymupdf
import os
from app.config.settings import config
from app.repository.file import FileRepository


class PDFParserService:
    def __init__(self, repository: Annotated[FileRepository, Depends()]):
        # self.parser = parser
        self.repository = repository

    async def retrieve_images(self, filename: str):
        # for *_, files in os.walk(config.BASE_FILES_DIR):
        #     # if [filename] in files:
        #     #     print(filename)
        #     for file in files:
        #         print(type(file))

        filepath = await self.repository.get_path(filename=filename)
        return filepath






from typing import Annotated

from fastapi import Depends

from app.repository.file import FileRepository


class PDFParserService:
    def __init__(
        self,
        repository: Annotated[FileRepository, Depends()],
        parser: Annotated[..., Depends()],
    ):
        self.parser = parser
        self.repository = repository

    async def retrieve_images(self, filename: str):
        filepath = await self.repository.get_path(filename=filename)
        return filepath

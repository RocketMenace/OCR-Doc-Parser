from typing import Annotated

from fastapi import Depends, UploadFile

from app.repository.file import FileRepository


class FileService:
    def __init__(self, repository: Annotated[FileRepository, Depends()]):
        self.repository = repository

    async def save(self, file: UploadFile):
        return await self.repository.save(file=file)

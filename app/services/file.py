from fastapi import UploadFile, Depends
from app.repository.file import FileRepository
from typing import Annotated


class FileService:

    def __init__(self, repository: Annotated[FileRepository, Depends()]):
        self.repository = repository

    async def save(self, file: UploadFile):
        return await self.repository.save(file=file)
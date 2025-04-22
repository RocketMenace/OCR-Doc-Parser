from typing import Annotated

from fastapi import APIRouter, Depends, UploadFile, status

from app.services.file import FileService

router = APIRouter(prefix="/files", tags=["Files"])


@router.post(path="/upload", status_code=status.HTTP_200_OK)
async def upload_file(file: UploadFile, service: Annotated[FileService, Depends()]):
    return await service.save(file)

from fastapi import APIRouter, Depends, status, UploadFile
from typing import Annotated
from app.services.parser import PDFParserService
from app.services.file import FileService

router = APIRouter(prefix="/files", tags=["Files"])


@router.post(path="/upload", status_code=status.HTTP_200_OK)
async def upload_dile(
    upload_file: UploadFile, service: Annotated[FileService, Depends()]
):
    return await service.save(upload_file)

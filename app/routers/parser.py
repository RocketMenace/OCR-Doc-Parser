from typing import Annotated

from fastapi import APIRouter, Depends, UploadFile, status

from app.services.parser import PDFParserService

router = APIRouter(prefix="/parse", tags=["Parser"])


@router.get(path="/pdf", status_code=status.HTTP_200_OK)
async def retrieve_images(
    filename: str, service: Annotated[PDFParserService, Depends()]
):
    return await service.retrieve_images(filename)

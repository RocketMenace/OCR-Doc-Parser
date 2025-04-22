from fastapi import APIRouter, Depends, status, UploadFile
from typing import Annotated
from app.services.parser import PDFParserService

router = APIRouter(prefix="/parse", tags=["Parser"])


@router.get(path="/pdf", status_code=status.HTTP_200_OK)
def retrieve_images(
    filename: str, service: Annotated[PDFParserService, Depends()]
):
    return service.retrieve_images(filename)




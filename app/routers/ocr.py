from typing import Annotated

from fastapi import APIRouter, Depends, UploadFile, status

from app.services.ocr import OCRService

router = APIRouter(prefix="/ocr", tags=["OCR"])


@router.post(path="/")
async def process_images(image: UploadFile, service: Annotated[OCRService, Depends()]):
    return await service.images_to_text(image)

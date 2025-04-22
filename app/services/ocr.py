from typing import Annotated

from fastapi import Depends, UploadFile
from mistralai import Mistral

from app.integrations.ocr import get_ai_model


class OCRService:
    def __init__(self, ocr: Annotated[Mistral, Depends(get_ai_model)]):
        self.ocr = ocr

    async def images_to_text(self, image: UploadFile):
        pass

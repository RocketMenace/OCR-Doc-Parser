from typing import Annotated
from fastapi import Depends
from mistralai import Mistral
from app.integrations.parser import get_ai_model


class PDFParserService:
    def __init__(self, ocr: Annotated[Mistral, Depends(get_ai_model)]):
        pass

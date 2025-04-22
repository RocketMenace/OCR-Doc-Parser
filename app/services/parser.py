from typing import Annotated
from fastapi import Depends
from mistralai import Mistral
from app.integrations.ocr import get_ai_model
import pymupdf
import os
from app.config.settings import config


class PDFParserService:
    def __init__(self, parser):
        self.parser = parser

    def retrieve_images(self, filename: str):
        for *_, files in os.walk(config.BASE_FILES_DIR):
            # if [filename] in files:
            #     print(filename)
            for file in files:
                print(type(file))





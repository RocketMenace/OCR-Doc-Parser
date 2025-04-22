from typing import Annotated

from fastapi import Depends
from mistralai import Mistral

from app.config.settings import config


async def get_ai_model():
    ai_model = Mistral(api_key=config.MISTRAL_API_KEY)


from mistralai import Mistral

from app.config.settings import config


async def get_ai_model() -> Mistral:
    return Mistral(api_key=config.MISTRAL_API_KEY)

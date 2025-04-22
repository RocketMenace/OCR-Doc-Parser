from aiopath import AsyncPath
from app.config.settings import config
from datetime import datetime


def get_upload_dir():
    return AsyncPath(config.BASE_FILES_DIR)
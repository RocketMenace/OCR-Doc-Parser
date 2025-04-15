from fastapi import UploadFile
from datetime import datetime
from aiopath import AsyncPath
from app.config.settings import config
import aiofiles


class FileService:

    async def save(self, file: UploadFile):
        today = datetime.now().strftime("%Y-%m-%d")
        upload_dir = AsyncPath(config.BASE_FILES_DIR) / today
        if not await AsyncPath.exists(upload_dir):
            await AsyncPath.mkdir(upload_dir)
        filepath = upload_dir / file.filename
        async with aiofiles.open(filepath, mode="wb") as buffer:
            await buffer.write(await file.read())
        return {"filename": file.filename, "date": today}
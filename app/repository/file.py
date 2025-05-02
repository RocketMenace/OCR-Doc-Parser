from datetime import datetime
from typing import Annotated, Any

import aiofiles
from aiopath import AsyncPath
from fastapi import Depends, UploadFile

from app.dependencies.file import get_upload_dir


class FileRepository:
    def __init__(self, upload_dir: Annotated[AsyncPath, Depends(get_upload_dir)]):
        self.upload_dir = upload_dir

    async def save(self, file: UploadFile) -> dict[str, Any]:
        date = datetime.now().strftime("%Y-%m-%d")
        self.upload_dir = self.upload_dir / date
        if not await AsyncPath.exists(self.upload_dir):
            await AsyncPath.mkdir(self.upload_dir)
        filepath = self.upload_dir / file.filename
        async with aiofiles.open(filepath, mode="wb") as buffer:
            await buffer.write(await file.read())
        return {"filename": file.filename, "type": file.content_type}

    async def get_path(self, filename: str) -> str | None:
        async for content in AsyncPath(self.upload_dir).rglob(filename):
            return str(content)
        return None

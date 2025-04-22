from fastapi import FastAPI

from app.routers import file, parser

app = FastAPI(title="PDF Document parser", root_path="/api")

app.include_router(file.router)
app.include_router(parser.router)

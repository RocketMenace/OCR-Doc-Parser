from fastapi import FastAPI
from app.routers import parser

app = FastAPI(title="PDF Document parser", root_path="/api")

app.include_router(parser.router)

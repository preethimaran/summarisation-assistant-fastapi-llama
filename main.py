from fastapi import FastAPI
from app.routes import summarise

app = FastAPI(title='Summarise Assistant')
app.include_router(summarise.router, prefix="/api")
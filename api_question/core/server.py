"""
Server - Main
"""
import uvicorn
from fastapi import FastAPI

from api_question.core.routers import router

app: FastAPI = FastAPI()

app.include_router(router, prefix='/processing', tags=['Processing'])


def main():
    uvicorn.run(app, port=8010)

if __name__ == '__main__':
    main()
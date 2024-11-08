import asyncio
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from src.api.router import router as router_api
import uvicorn

origins = [
    'http://localhost',
    'http://127.0.0.1',
    'http://localhost:5173',
    'http://127.0.0.1:5173',
    'http://localhost:5173/',
    'http://127.0.0.1:5173/'
]

app = FastAPI()
app.include_router(router_api)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

async def start_server():
    uvicorn.run('main:app', host='127.0.0.1', port=5000, log_level='debug', use_colors=True, reload=True)

if __name__ == '__main__':
    asyncio.run(start_server())
from fastapi import APIRouter
from src.api.v1.router import router as router_v1

router = APIRouter(
    prefix='/api',
)

router.include_router(router_v1)
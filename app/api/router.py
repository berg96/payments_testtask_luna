from fastapi import APIRouter, Depends

from .auth import verify_api_key
from .schemas import ErrorResponse
from .v1.router import router as v1_router

main_router = APIRouter(
    prefix="/api",
    dependencies=[Depends(verify_api_key)],
    responses={401: {"model": ErrorResponse, "description": "Пользователь не авторизован"}},
)

main_router.include_router(v1_router)

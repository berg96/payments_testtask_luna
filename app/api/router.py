from fastapi import APIRouter, Depends

from .auth import verify_api_key
from .v1.router import router as v1_router

main_router = APIRouter(prefix="/api", dependencies=[Depends(verify_api_key)])

main_router.include_router(v1_router)

from fastapi import APIRouter, Depends
from v1.router import router as v1_router

from .auth import verify_auth_token

main_router = APIRouter(prefix="/api", dependencies=[Depends(verify_auth_token)])

main_router.include_router(v1_router)

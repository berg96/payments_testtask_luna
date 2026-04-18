from fastapi import APIRouter

from app.api.v1.endpoints import payments

router = APIRouter(prefix="/v1")
router.include_router(payments.router)

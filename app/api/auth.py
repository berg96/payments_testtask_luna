import secrets
from typing import Optional

from fastapi import HTTPException, Security, status
from fastapi.security import APIKeyHeader

from app.config.settings import settings

_api_key_header = APIKeyHeader(name="X-API-Key", auto_error=False)


def verify_api_key(key: Optional[str] = Security(_api_key_header)) -> None:
    if not key or not secrets.compare_digest(key, settings.API_KEY):
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "Unauthorized")

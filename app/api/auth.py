from fastapi import HTTPException, Security, status
from fastapi.security import APIKeyHeader

from app.config.settings import settings

_api_key_header = APIKeyHeader(name="X-API-Key", auto_error=False)


def verify_api_key(key: str | None = Security(_api_key_header)) -> None:
    if not key or key != settings.API_KEY:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "Unauthorized")

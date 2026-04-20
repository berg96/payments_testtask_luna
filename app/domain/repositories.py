from typing import Optional, Protocol
from uuid import UUID

from app.domain.entities import Payment


class PaymentRepository(Protocol):
    async def create(self, payment: Payment) -> Payment: ...

    async def get_by_id(self, id: UUID) -> Optional[Payment]: ...

    async def get_by_idempotency_key(self, key: str) -> Optional[Payment]: ...

from typing import Optional, Protocol

from app.domain.entities.payment import Payment


class PaymentRepository(Protocol):
    async def create(self, payment: Payment) -> Payment: ...

    async def get_by_idempotency_key(self, key: str) -> Optional[Payment]: ...

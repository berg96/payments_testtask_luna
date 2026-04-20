from app.domain.entities.payment import Payment
from app.domain.repositories import PaymentRepository


class CreatePaymentUseCase:
    def __init__(self, repo: PaymentRepository) -> None:
        self._repo = repo

    async def execute(self, payment: Payment) -> Payment:
        existing = await self._repo.get_by_idempotency_key(payment.idempotency_key)
        if existing:
            return existing
        return await self._repo.create(payment)

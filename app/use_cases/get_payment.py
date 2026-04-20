from uuid import UUID

from app.domain.entities import Payment
from app.domain.exceptions import PaymentNotFound
from app.domain.repositories import PaymentRepository


class GetPaymentUseCase:
    def __init__(self, repo: PaymentRepository) -> None:
        self._repo = repo

    async def execute(self, id: UUID) -> Payment:
        payment = await self._repo.get_by_id(id)
        if payment is None:
            raise PaymentNotFound(identifier=id)
        return payment

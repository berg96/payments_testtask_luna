from typing import Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.entities.payment import Payment as PaymentEntity
from app.domain.repositories import PaymentRepository
from app.infrastructure.db.models.payment import Payment as PaymentModel


def _from_orm(payment_model: PaymentModel) -> PaymentEntity:
    return PaymentEntity(
        id=payment_model.id,
        idempotency_key=payment_model.idempotency_key,
        amount=payment_model.amount,
        currency=payment_model.currency,
        description=payment_model.description,
        payment_metadata=payment_model.payment_metadata or {},
        status=payment_model.status,
        webhook_url=payment_model.webhook_url,
        created_at=payment_model.created_at,
        processed_at=payment_model.processed_at,
    )


def _to_orm(payment_entity: PaymentEntity) -> PaymentModel:
    return PaymentModel(
        id=payment_entity.id,
        idempotency_key=payment_entity.idempotency_key,
        amount=payment_entity.amount,
        currency=payment_entity.currency,
        description=payment_entity.description,
        payment_metadata=payment_entity.payment_metadata,
        status=payment_entity.status,
        webhook_url=payment_entity.webhook_url,
        processed_at=payment_entity.processed_at,
    )


class SqlAlchemyPaymentRepository(PaymentRepository):
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def create(self, payment: PaymentEntity) -> PaymentEntity:
        model = _to_orm(payment)
        self._session.add(model)
        await self._session.flush()
        await self._session.refresh(model)
        return _from_orm(model)

    async def get_by_idempotency_key(self, key: str) -> Optional[PaymentEntity]:
        stmt = select(PaymentModel).where(PaymentModel.idempotency_key == key)
        model = (await self._session.execute(stmt)).scalar_one_or_none()
        return _from_orm(model) if model else None

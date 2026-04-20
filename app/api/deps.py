from typing import AsyncGenerator

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.repositories import PaymentRepository
from app.infrastructure.db import async_session_maker
from app.infrastructure.db.repositories import SqlAlchemyPaymentRepository
from app.use_cases.create_payment import CreatePaymentUseCase


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as async_session:
        try:
            yield async_session
        except Exception:
            await async_session.rollback()
            raise
        else:
            await async_session.commit()


async def get_payment_repo(session: AsyncSession = Depends(get_async_session)) -> PaymentRepository:
    return SqlAlchemyPaymentRepository(session)


async def get_create_payment_usecase(repo: PaymentRepository = Depends(get_payment_repo)) -> CreatePaymentUseCase:
    return CreatePaymentUseCase(repo)

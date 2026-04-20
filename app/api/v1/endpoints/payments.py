from fastapi import APIRouter, Depends, Header, status

from app.api.deps import get_create_payment_usecase
from app.api.schemas import ErrorResponse
from app.api.v1.schemas.payment import PaymentAccepted, PaymentCreate
from app.domain.entities.payment import Payment
from app.use_cases.create_payment import CreatePaymentUseCase

router = APIRouter(prefix="/payments", tags=["Payments v1"])


@router.post(
    "",
    response_model=PaymentAccepted,
    status_code=status.HTTP_202_ACCEPTED,
    summary="Создание платежа",
    responses={
        401: {"model": ErrorResponse, "description": "Пользователь не авторизован"},
        500: {"model": ErrorResponse, "description": "Внутренняя ошибка сервера"},
    },
)
async def create_payment(
    data: PaymentCreate,
    idempotency_key: str = Header(..., alias="Idempotency-Key"),
    use_case: CreatePaymentUseCase = Depends(get_create_payment_usecase),
) -> PaymentAccepted:
    payment = Payment(
        idempotency_key=idempotency_key,
        amount=data.amount,
        currency=data.currency,
        description=data.description,
        webhook_url=str(data.webhook_url),
        payment_metadata=data.metadata,
    )
    result = await use_case.execute(payment)
    return PaymentAccepted(
        payment_id=result.id,
        status=result.status,
        created_at=result.created_at,
    )

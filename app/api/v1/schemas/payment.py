from datetime import datetime
from decimal import Decimal
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, Field, HttpUrl

from app.domain.entities import Payment
from app.domain.enums import CurrencyEnum, PaymentStatusEnum


class PaymentCreate(BaseModel):
    amount: Decimal = Field(..., gt=0, max_digits=18, decimal_places=2, description="Сумма платежа")
    currency: CurrencyEnum = Field(..., description="Валюта")
    description: str = Field(..., min_length=1, max_length=500, description="Описание платежа")
    metadata: dict = Field(default_factory=dict, description="Мета-данные")
    webhook_url: HttpUrl = Field(..., description="Webhook URL для уведомления о результате")


class PaymentAccepted(BaseModel):
    payment_id: UUID = Field(..., description="Уникальный идентификатор платежа")
    status: PaymentStatusEnum = Field(..., description="Статус платежа")
    created_at: datetime = Field(..., description="Время и дата создания платежа")


class PaymentResponse(BaseModel):
    id: UUID = Field(..., description="Уникальный идентификатор платежа")
    amount: Decimal = Field(..., description="Сумма платежа")
    currency: CurrencyEnum = Field(..., description="Валюта")
    description: str = Field(..., description="Описание платежа")
    metadata: dict = Field(default_factory=dict, description="Мета-данные")
    status: PaymentStatusEnum = Field(..., description="Статус платежа")
    webhook_url: str = Field(..., description="Webhook URL для уведомления о результате")
    idempotency_key: str = Field(..., description="Ключ идемпотентности")
    created_at: datetime = Field(..., description="Время и дата создания платежа")
    processed_at: Optional[datetime] = Field(None, description="Время и дата обработки платежа")

    @classmethod
    def from_entity(cls, payment: Payment) -> "PaymentResponse":
        return cls(
            id=payment.id,
            amount=payment.amount,
            currency=payment.currency,
            description=payment.description,
            metadata=payment.payment_metadata,
            status=payment.status,
            webhook_url=payment.webhook_url,
            idempotency_key=payment.idempotency_key,
            created_at=payment.created_at,
            processed_at=payment.processed_at,
        )

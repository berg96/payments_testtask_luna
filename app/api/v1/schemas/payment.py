from datetime import datetime
from decimal import Decimal
from uuid import UUID

from pydantic import BaseModel, Field, HttpUrl

from app.domain.enums import CurrencyEnum, PaymentStatusEnum


class PaymentCreate(BaseModel):
    amount: Decimal = Field(..., gt=0, max_digits=18, decimal_places=2, description="Сумма")
    currency: CurrencyEnum = Field(..., description="Валюта")
    description: str = Field(..., min_length=1, max_length=500, description="Описание платежа")
    metadata: dict = Field(default_factory=dict, description="Мета-данные")
    webhook_url: HttpUrl = Field(..., description="Webhook URL для уведомления о результате")


class PaymentAccepted(BaseModel):
    payment_id: UUID = Field(..., description="Уникальный идентификатор платежа")
    status: PaymentStatusEnum = Field(..., description="Статус платежа")
    created_at: datetime = Field(..., description="Время и дата создания платежа")

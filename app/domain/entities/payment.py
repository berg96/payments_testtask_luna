from dataclasses import dataclass, field
from datetime import datetime
from decimal import Decimal
from typing import Optional
from uuid import UUID, uuid4

from app.domain.enums import CurrencyEnum, PaymentStatusEnum


@dataclass
class Payment:
    amount: Decimal
    currency: CurrencyEnum
    description: str
    webhook_url: str
    idempotency_key: str
    id: UUID = field(default_factory=uuid4)
    payment_metadata: dict = field(default_factory=dict)
    status: PaymentStatusEnum = PaymentStatusEnum.PENDING
    created_at: Optional[datetime] = None
    processed_at: Optional[datetime] = None

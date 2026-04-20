from dataclasses import dataclass, field
from datetime import datetime
from decimal import Decimal
from typing import Optional
from uuid import UUID, uuid4

from app.domain.enums import CurrencyEnum, PaymentStatusEnum


@dataclass
class Payment:
    idempotency_key: str
    amount: Decimal
    currency: CurrencyEnum
    description: str
    webhook_url: str
    id: UUID = field(default_factory=uuid4)
    status: PaymentStatusEnum = PaymentStatusEnum.PENDING
    payment_metadata: dict = field(default_factory=dict)
    created_at: Optional[datetime] = None
    processed_at: Optional[datetime] = None

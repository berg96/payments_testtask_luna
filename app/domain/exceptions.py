from typing import Optional, Union
from uuid import UUID


class NotFoundError(Exception):
    resource: Optional[str] = "Resource"
    message_template: str = "{resource} ({identifier}) not found"

    def __init__(self, *, resource: Optional[str] = None, identifier: Union[str, int, UUID, None] = None):
        self.resource = resource or self.resource
        self.identifier = identifier
        super().__init__(self.message_template.format(resource=self.resource, identifier=self.identifier))


class PaymentNotFound(NotFoundError):
    resource = "Payment"

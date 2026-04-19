import datetime

from sqlalchemy import DateTime, MetaData, func
from sqlalchemy.orm import DeclarativeBase, Mapped, declared_attr, mapped_column

from app.config.settings import settings


class Base(DeclarativeBase):
    metadata = MetaData(schema=settings.DB_SCHEMA)

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower() + "s"


class TimestampMixin:
    created_at: Mapped[datetime.datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

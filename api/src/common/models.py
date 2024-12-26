from datetime import datetime, timezone
from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, declared_attr


# Model Class
class Base(DeclarativeBase):
    @declared_attr.cascading
    @classmethod
    def id(cls):
        for base in cls.__mro__[1:-1]:
            if getattr(base, "__table__", None) is not None:
                return mapped_column(ForeignKey(base.id), primary_key=True)
            else:
                return mapped_column(Integer, primary_key=True)


""" class Audit:
    __abstract__ = True
    created_at: Mapped[datetime] = mapped_column(
        default=lambda: datetime.now(timezone.utc)
    )
    updated_at: Mapped[datetime] = mapped_column(
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
    ) """

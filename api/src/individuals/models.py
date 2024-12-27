from .. import db
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String


class Person(db.Model):
    __tablename__ = "people"
    # id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(60),nullable=False)
    lastname: Mapped[str] = mapped_column(String(60), nullable=False)
    dni: Mapped[str] = mapped_column(String(10), nullable=False, unique=True)
    phone: Mapped[str] = mapped_column(String(17))
    email: Mapped[str] = mapped_column(String(60), nullable=False, unique=True)
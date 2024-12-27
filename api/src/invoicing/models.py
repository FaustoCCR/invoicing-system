from .. import db
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, String, Float, Integer
from datetime import datetime, timezone


class PaymentType(db.Model):
    __tablename__ = "payment_types"
    type: Mapped[str] = mapped_column(String(30), nullable=False, unique=True)
    description: Mapped[str] = mapped_column(String(80))

    # relationship
    invoices = relationship("Invoice", back_populates="payment_type")


# association table
invoice_items = db.Table(
    "invoice_items",
    db.Model.metadata,
    db.Column("invoice_id", Integer, ForeignKey("invoices.id")),
    db.Column("product_id", Integer, ForeignKey("products.id")),
    db.Column("quantity", Integer, nullable=False),
    db.Column("price", Float, nullable=False),
    db.Column("subtotal", Float, nullable=False),
)


class Invoice(db.Model):
    __tablename__ = "invoices"
    ruc: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(
        default=lambda: datetime.now(timezone.utc)
    )
    discount: Mapped[float]
    total: Mapped[float]

    # FKs
    person_id: Mapped[int] = mapped_column(ForeignKey("people.id"))
    payment_type_id: Mapped[int] = mapped_column(ForeignKey("payment_types.id"))

    # relationships
    person = relationship("Person", back_populates="invoices")
    payment_type = relationship("PaymentType", back_populates="invoices")

    # products = relationship("Product", secondary=invoice_items, back_populates="invoices")
    products = relationship("Product", secondary=invoice_items)

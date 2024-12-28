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
""" invoice_items = db.Table(
    "invoice_items",
    db.Model.metadata,
    db.Column("invoice_id", Integer, ForeignKey("invoices.id")),
    db.Column("product_id", Integer, ForeignKey("products.id")),
    db.Column("quantity", Integer, nullable=False),
    db.Column("price", Float, nullable=False),
    db.Column("subtotal", Float, nullable=False),
)
 """
class InvoiceItem(db.Model):
    __tablename__ = "invoice_items"

    # FKs
    invoice_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("invoices.id"), nullable=False
    )
    product_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("products.id"), nullable=False
    )

    quantity: Mapped[int] = mapped_column(Integer, nullable=False)
    price: Mapped[float] = mapped_column(Float(precision=2), nullable=False)
    subtotal: Mapped[float] = mapped_column(Float(precision=2), nullable=False)

    # relationships
    invoice = relationship("Invoice", back_populates="items")
    product = relationship("Product", back_populates="invoices")


class Invoice(db.Model):
    __tablename__ = "invoices"
    ruc: Mapped[str] = mapped_column(String(13), nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        default=lambda: datetime.now(timezone.utc)
    )
    discount: Mapped[float] = mapped_column(
        Float(precision=2), nullable=False, default=0.0
    )
    total: Mapped[float] = mapped_column(Float(precision=2), nullable=False)

    # FKs
    person_id: Mapped[int] = mapped_column(ForeignKey("people.id"), nullable=False)
    payment_type_id: Mapped[int] = mapped_column(
        ForeignKey("payment_types.id"), nullable=False
    )

    # relationships
    person = relationship("Person", back_populates="invoices")
    payment_type = relationship("PaymentType", back_populates="invoices")
    items = relationship("InvoiceItem", back_populates="invoice")

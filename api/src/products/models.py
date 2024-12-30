from .. import db
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, String, Boolean, Integer, Float


class Classification(db.Model):
    __tablename__ = "classifications"

    group: Mapped[str] = mapped_column(String(60), unique=True)

    # One-to-many relationship with Product
    products = relationship("Product", back_populates="classification")


class Supplier(db.Model):
    __tablename__ = "suppliers"
    ruc: Mapped[str] = mapped_column(String(13), unique=True)
    phone: Mapped[str] = mapped_column(String(17), unique=True)
    country: Mapped[str] = mapped_column(String(3))
    email: Mapped[str] = mapped_column(String(60), nullable=False, unique=True)
    currency: Mapped[str] = mapped_column(String(3))

    # One-to-many relationship with Product
    products = relationship("Product", back_populates="supplier")


class Product(db.Model):
    __tablename__ = "products"
    name: Mapped[str] = mapped_column(String(60), nullable=False)
    stock: Mapped[int] = mapped_column(Integer(), nullable=False)
    unit_price: Mapped[float] = mapped_column(Float(precision=2), nullable=False)
    unit: Mapped[str] = mapped_column(String(20), nullable=False)
    tax: Mapped[bool] = mapped_column(Boolean(), default=True)

    classification_id: Mapped[int] = mapped_column(
        ForeignKey("classifications.id"), nullable=False
    )
    supplier_id: Mapped[int] = mapped_column(ForeignKey("suppliers.id"), nullable=False)

    # relationships
    classification = relationship("Classification", back_populates="products")
    supplier = relationship("Supplier", back_populates="products")
    invoices = relationship("InvoiceItem", back_populates="product")

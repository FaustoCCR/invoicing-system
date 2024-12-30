from .. import ma
from .models import PaymentType, Invoice, InvoiceItem
from marshmallow_sqlalchemy.fields import Nested


class PaymentTypeSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = PaymentType


class InvoiceItemSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = InvoiceItem
        include_fk = True

    price = ma.auto_field(dump_only=True)
    subtotal = ma.auto_field(dump_only=True)


class InvoiceSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Invoice
        include_fk = True
        # include_relationships = True

    total = ma.auto_field(dump_only=True)
    items = Nested(
        InvoiceItemSchema,
        many=True,
        exclude=(
            "id",
            "invoice_id",
        ),
    )

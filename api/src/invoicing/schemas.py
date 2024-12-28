from .. import ma
from .models import PaymentType, Invoice


class PaymentTypeSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = PaymentType


class InvoiceSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Invoice
        include_fk = True
        include_relationships = True

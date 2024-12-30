from .models import Invoice, InvoiceItem
from ..products.models import Product
from src.common.services import AbstractService
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from apiflask import abort


class InvoiceService(AbstractService):
    def __init__(self, session: Session):
        self.session = session

    def get_all(self):
        return Invoice.query.all()

    def get_by_id(self, id):
        return Invoice.query.get_or_404(id)

    def update(self, id, data):
        return super().update(id, data)

    def delete(self, id):
        item = self.get_by_id(id)
        self.session.delete(item)
        self.session.commit()

    def create(self, data):
        try:
            new_invoice = Invoice(
                ruc=data.get("ruc"),
                payment_type_id=data.get("payment_type_id"),
                person_id=data.get("person_id"),
                discount=data.get("discount", 0),
                total=data.get("total", 0),
            )
            total = 0.0
            for item in data.get("items"):
                product = Product.query.get_or_404(item["product_id"])
                quantity = item["quantity"]
                unit_price = product.unit_price
                subtotal = quantity * unit_price

                invoice_item = InvoiceItem(
                    product_id=product.id,
                    quantity=quantity,
                    price=unit_price,
                    subtotal=subtotal,
                )
                new_invoice.items.append(invoice_item)
                total += subtotal
            new_invoice.total = total - new_invoice.discount
            self.session.add(new_invoice)
            self.session.commit()
            return new_invoice

        except IntegrityError as e:
            self.session.rollback()
            # print("err:", e)
            abort(400, message="Integrity error occurred. Please check your data")

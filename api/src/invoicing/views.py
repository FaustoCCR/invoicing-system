from src import db
from .models import PaymentType
from .schemas import InvoiceSchema, PaymentTypeSchema
from .services import InvoiceService
from apiflask import APIBlueprint
from flask.views import MethodView
from ..auth.services import auth
from src.common.repository import SQLAlchemyRepository
from src.common.services import Service

invoices_bp = APIBlueprint("invoices", __name__, url_prefix="/invoices")
payment_type_bp = APIBlueprint("payment-type", __name__, url_prefix="/payment-type")


# dependencies
invoice_service = InvoiceService(session=db.session)

payment_type_repository = SQLAlchemyRepository[PaymentType, int](
    db.session, PaymentType
)
payment_type_service = Service(payment_type_repository)


class InvoiceItemView(MethodView):

    decorators = [invoices_bp.auth_required(auth)]

    @invoices_bp.output(InvoiceSchema)
    def get(self, id):
        return invoice_service.get_by_id(id)

    @invoices_bp.output({}, status_code=204)
    def delete(self, id):
        return invoice_service.delete(id)


class InvoiceGroupView(MethodView):
    decorators = [invoices_bp.auth_required(auth)]

    @invoices_bp.output(InvoiceSchema(many=True))
    def get(self):
        return invoice_service.get_all()

    @invoices_bp.input(InvoiceSchema)
    @invoices_bp.output(InvoiceSchema, status_code=201)
    def post(self, json_data):
        return invoice_service.create(json_data)


invoices_bp.add_url_rule(
    "/<int:id>", view_func=InvoiceItemView.as_view("invoices-item")
)
invoices_bp.add_url_rule("", view_func=InvoiceGroupView.as_view("invoices-group"))


class PaymentTypeItemView(MethodView):

    decorators = [payment_type_bp.auth_required(auth)]

    @payment_type_bp.output(PaymentTypeSchema)
    def get(self, id):
        return payment_type_service.get_by_id(id)

    @payment_type_bp.output({}, status_code=204)
    def delete(self, id):
        return payment_type_service.delete(id)


class PaymentTypeGroupView(MethodView):
    decorators = [payment_type_bp.auth_required(auth)]

    @payment_type_bp.output(PaymentTypeSchema(many=True))
    def get(self):
        return payment_type_service.get_all()

    @payment_type_bp.input(PaymentTypeSchema)
    @payment_type_bp.output(PaymentTypeSchema, status_code=201)
    def post(self, json_data):
        return payment_type_service.create(json_data)


payment_type_bp.add_url_rule(
    "/<int:id>", view_func=PaymentTypeItemView.as_view("payment-type-item")
)
payment_type_bp.add_url_rule(
    "", view_func=PaymentTypeGroupView.as_view("payment-type-group")
)

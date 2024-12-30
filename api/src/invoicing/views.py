from src import db
from .schemas import InvoiceSchema
from .services import InvoiceService
from apiflask import APIBlueprint
from flask.views import MethodView
from ..auth.services import auth


invoices_bp = APIBlueprint("invoices", __name__, url_prefix="/invoices")

# dependencies
service = InvoiceService(session=db.session)


class InvoiceItemView(MethodView):

    decorators = [invoices_bp.auth_required(auth)]

    @invoices_bp.output(InvoiceSchema)
    def get(self, id):
        return service.get_by_id(id)

    @invoices_bp.output({}, status_code=204)
    def delete(self, id):
        return service.delete(id)


class InvoiceGroupView(MethodView):
    decorators = [invoices_bp.auth_required(auth)]

    @invoices_bp.output(InvoiceSchema(many=True))
    def get(self):
        return service.get_all()

    @invoices_bp.input(InvoiceSchema)
    @invoices_bp.output(InvoiceSchema, status_code=201)
    def post(self, json_data):
        return service.create(json_data)


invoices_bp.add_url_rule(
    "/<int:id>", view_func=InvoiceItemView.as_view("invoices-item")
)
invoices_bp.add_url_rule("", view_func=InvoiceGroupView.as_view("invoices-group"))

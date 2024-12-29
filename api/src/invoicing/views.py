from src import db
from .schemas import InvoiceSchema
from .services import InvoiceService
from apiflask import APIBlueprint
from flask.views import MethodView
from src.common.repository import SQLAlchemyRepository
from src.common.services import Service

invoices_bp = APIBlueprint("invoices", __name__, url_prefix="/invoices")

# dependencies
""" repository = SQLAlchemyRepository[Invoice, int](db.session, Invoice)
service = Service(repository) """
service = InvoiceService(session=db.session)


class InvoiceGroupView(MethodView):
    @invoices_bp.output(InvoiceSchema(many=True))
    def get(self):
        return service.get_all()

    @invoices_bp.input(InvoiceSchema)
    @invoices_bp.output(InvoiceSchema, status_code=201)
    def post(self, json_data):
        print(json_data)
        return service.create(json_data)


invoices_bp.add_url_rule("", view_func=InvoiceGroupView.as_view("invoices"))

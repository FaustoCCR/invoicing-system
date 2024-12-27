from apiflask import APIBlueprint
from flask.views import MethodView
from ..models import Supplier
from ..schemas import SupplierSchema
from src.common.repository import SQLAlchemyRepository
from src.common.services import Service
from src import db


bp = APIBlueprint("suppliers", __name__, url_prefix="/suppliers")

# dependencies
repository = SQLAlchemyRepository[Supplier, int](db.session, Supplier)
service = Service(repository)


class SuppliersGroupView(MethodView):
    @bp.output(SupplierSchema(many=True))
    def get(self):
        return service.get_all()

    @bp.input(SupplierSchema)
    @bp.output(SupplierSchema, status_code=201)
    def post(self, json_data):
        return service.create(json_data)


bp.add_url_rule("", view_func=SuppliersGroupView.as_view("suppliers"))

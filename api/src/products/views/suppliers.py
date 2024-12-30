from apiflask import APIBlueprint
from flask.views import MethodView
from ..models import Supplier
from ..schemas import SupplierSchema
from src.common.repository import SQLAlchemyRepository
from src.common.services import Service
from src import db
from src.auth.services import auth


bp = APIBlueprint("suppliers", __name__, url_prefix="/suppliers")

# dependencies
repository = SQLAlchemyRepository[Supplier, int](db.session, Supplier)
service = Service(repository)


class SuppliersItemView(MethodView):

    decorators = [bp.auth_required(auth)]

    @bp.output(SupplierSchema)
    def get(self, id):
        return service.get_by_id(id)

    @bp.input(SupplierSchema, location="json")
    @bp.output(SupplierSchema)
    def put(self, id, json_data):
        return service.update(id, json_data)

    @bp.output({}, status_code=204)
    def delete(self, id):
        return service.delete(id)


class SuppliersGroupView(MethodView):

    decorators = [bp.auth_required(auth)]

    @bp.output(SupplierSchema(many=True))
    def get(self):
        return service.get_all()

    @bp.input(SupplierSchema)
    @bp.output(SupplierSchema, status_code=201)
    def post(self, json_data):
        return service.create(json_data)


bp.add_url_rule("/<int:id>", view_func=SuppliersItemView.as_view("suppliers-item"))
bp.add_url_rule("", view_func=SuppliersGroupView.as_view("suppliers-group"))

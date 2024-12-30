from apiflask import APIBlueprint
from flask.views import MethodView
from ..schemas import ProductSchema
from ..models import Product
from src.common.repository import SQLAlchemyRepository
from src.common.services import Service
from src import db
from src.auth.services import auth


bp = APIBlueprint("products", __name__, url_prefix="/products")

# dependencies
repository = SQLAlchemyRepository[Product, int](db.session, Product)
service = Service(repository)


class ProductsItemView(MethodView):

    decorators = [bp.auth_required(auth)]

    @bp.output(ProductSchema)
    def get(self, id):
        return service.get_by_id(id)

    @bp.input(ProductSchema, location="json")
    @bp.output(ProductSchema)
    def put(self, id, json_data):
        return service.update(id, json_data)

    @bp.output({}, status_code=204)
    def delete(self, id):
        return service.delete(id)


class ProductsView(MethodView):

    decorators = [bp.auth_required(auth)]

    @bp.output(ProductSchema(many=True))
    def get(self):
        return service.get_all()

    @bp.input(ProductSchema)
    @bp.output(ProductSchema, status_code=201)
    def post(self, json_data):
        return service.create(json_data)


bp.add_url_rule("/<int:id>", view_func=ProductsItemView.as_view("products-item"))
bp.add_url_rule("", view_func=ProductsView.as_view("products-group"))

from apiflask import APIBlueprint
from flask.views import MethodView
from ..schemas import ProductSchema
from ..models import Product
from src.common.repository import SQLAlchemyRepository
from src.common.services import Service
from src import db


bp = APIBlueprint("products", __name__, url_prefix="/products")

# dependencies
repository = SQLAlchemyRepository[Product, int](db.session, Product)
service = Service(repository)


class ProductsView(MethodView):
    @bp.output(ProductSchema(many=True))
    def get(self):
        return service.get_all()

    @bp.input(ProductSchema)
    @bp.output(ProductSchema, status_code=201)
    def post(self, json_data):
        return service.create(json_data)


bp.add_url_rule("", view_func=ProductsView.as_view("products"))

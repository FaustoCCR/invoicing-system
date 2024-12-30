from apiflask import APIBlueprint
from flask.views import MethodView
from ..models import Classification
from ..schemas import ClassificationSchema
from src.common.repository import SQLAlchemyRepository
from src.common.services import Service
from src import db
from src.auth.services import auth


bp = APIBlueprint("classifications", __name__, url_prefix="/classifications")

# dependencies
repository = SQLAlchemyRepository[Classification, int](db.session, Classification)
service = Service(repository)


class ClassificationItemView(MethodView):

    decorators = [bp.auth_required(auth)]

    @bp.output(ClassificationSchema)
    def get(self, id):
        return service.get_by_id(id)

    @bp.input(ClassificationSchema, location="json")
    @bp.output(ClassificationSchema)
    def put(self, id, json_data):
        return service.update(id, json_data)

    @bp.output({}, status_code=204)
    def delete(self, id):
        return service.delete(id)


class ClassificationGroupView(MethodView):

    decorators = [bp.auth_required(auth)]

    @bp.output(ClassificationSchema(many=True))
    def get(self):
        return service.get_all()

    @bp.input(ClassificationSchema)
    @bp.output(ClassificationSchema(exclude=("products",)), status_code=201)
    def post(self, json_data):
        return service.create(json_data)


bp.add_url_rule(
    "/<int:id>", view_func=ClassificationItemView.as_view("classifications-item")
)
bp.add_url_rule("", view_func=ClassificationGroupView.as_view("classifications-group"))

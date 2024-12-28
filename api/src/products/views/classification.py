from apiflask import APIBlueprint
from flask.views import MethodView
from ..models import Classification
from ..schemas import ClassificationSchema
from src.common.repository import SQLAlchemyRepository
from src.common.services import Service
from src import db


bp = APIBlueprint("classifications", __name__, url_prefix="/classifications")

# dependencies
repository = SQLAlchemyRepository[Classification, int](db.session, Classification)
service = Service(repository)


class ClassificationGroupView(MethodView):
    @bp.output(ClassificationSchema(many=True))
    def get(self):
        return service.get_all()

    @bp.input(ClassificationSchema)
    @bp.output(ClassificationSchema(exclude=("products",)), status_code=201)
    def post(self, json_data):
        return service.create(json_data)


bp.add_url_rule("", view_func=ClassificationGroupView.as_view("classifications"))

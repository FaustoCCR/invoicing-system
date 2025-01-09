from .. import db
from .schemas import PersonSchema
from .models import Person
from .repository import PeopleRepository
from .services import PeopleService
from flask.views import MethodView
from apiflask import APIBlueprint
from ..auth.services import auth


bp = APIBlueprint("people", __name__, url_prefix="/people")

# repository = SQLAlchemyRepository[Person, int](session=db.session, model=Person)
repository = PeopleRepository(session=db.session)
service = PeopleService(repository)


class PersonView(MethodView):

    decorators = [bp.auth_required(auth)]

    def _get_item(self, id):
        return Person.query.get_or_404(id)

    @bp.auth_required(auth)
    @bp.output(PersonSchema)
    def get(self, id: int):
        return self._get_item(id)

    @bp.input(PersonSchema, location="json")
    @bp.output(PersonSchema)
    def put(self, id, json_data):
        return service.update(id, json_data)

    @bp.output({}, status_code=204)
    def delete(self, id):
        return service.delete(id)


class PeopleView(MethodView):

    @bp.auth_required(auth)
    @bp.output(PersonSchema(many=True))
    def get(self):
        # return Person.query.all()
        # return db.session.query(Person).all()
        # return repository.find_all()
        return service.get_all()

    @bp.input(PersonSchema, location="json")
    @bp.output(PersonSchema, status_code=201)
    def post(self, json_data):
        """new_person = Person(**json_data)
        db.session.add(new_person)
        db.session.commit()
        return json_data"""
        # new_person = Person(**json_data)
        # return repository.add(item=new_person)
        return service.create(json_data)


bp.add_url_rule("/<int:id>", view_func=PersonView.as_view("person"))
bp.add_url_rule("", view_func=PeopleView.as_view("people"))

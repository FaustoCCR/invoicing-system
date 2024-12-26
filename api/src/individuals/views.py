from .schemas import PersonSchema
from .models import Person
from .repository import PeopleRepository
from .services import CustomPeopleService, PeopleService
from flask.views import MethodView
from apiflask import APIBlueprint
from .. import db

bp = APIBlueprint("people", __name__, url_prefix="/people")

# repository = SQLAlchemyRepository[Person, int](session=db.session, model=Person)
repository = PeopleRepository(session=db.session)
# service = PeopleService(repository)
service = CustomPeopleService(repository)


class PersonView(MethodView):
    @bp.output(PersonSchema)
    def get(self, id: int):
        return Person.query.get_or_404(id)


class PeopleView(MethodView):
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

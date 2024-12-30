from src.common.repository import SQLAlchemyRepository
from .models import Person


class PeopleRepository(SQLAlchemyRepository[Person, int]):

    def __init__(self, session):
        super().__init__(session, Person)

    def find_by_dni(self, dni: str):
        return self.session.query(self.model).filter(Person.dni == dni).first()

    def find_by_email(self, email: str):
        return self.session.query(self.model).filter(Person.email == email).first()

from src.common.services import Service, AbstractService
from .repository import PeopleRepository


""" class CustomPeopleService(AbstractService):
    # A custom service could englobe more logic (repositories, models, etc)
    def __init__(self, people_repository: PeopleRepository):
        self.people_repository = people_repository

    def create(self, data):
        instance = self.people_repository.model(**data)
        return self.people_repository.add(instance)
    def get_all(self):
        return super().get_all()
    def get_by_id(self, id):
        return super().get_by_id(id)
    def update(self, id, data):
        return super().update(id, data)
    def delete(self, id):
        return super().delete(id) """


class PeopleService(Service):
    pass

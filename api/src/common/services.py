from abc import ABC, abstractmethod
from .repository import AbstractRepository


class AbstractService(ABC):
    @abstractmethod
    def create(self, data: dict):
        pass

    @abstractmethod
    def get_by_id(self, id):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def update(self, id, data: dict):
        pass

    @abstractmethod
    def delete(self, id):
        pass


class Service(AbstractService):
    def __init__(self, repository: AbstractRepository):
        self.repository = repository

    def create(self, data: dict):
        instance = self.repository.model(**data)
        return self.repository.add(instance)

    def get_by_id(self, id):
        return self.repository.find_by_id(id)

    def get_all(self):
        return self.repository.find_all()

    def update(self, id, data: dict):
        item = self.get_by_id(id)
        for attr, value in data.items():
            setattr(item, attr, value)
        return self.repository.update(item)

    def delete(self, id):
        return self.repository.delete_by_id(id)

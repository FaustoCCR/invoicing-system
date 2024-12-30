from src.common.services import AbstractService
from .repositories import UserRepository
from src import bcrypt


class UserService(AbstractService):
    def __init__(self, repository: UserRepository):
        self.repository = repository

    def get_all(self):
        return self.repository.find_all()

    def get_by_id(self, id):
        return self.repository.find_by_id(id)

    def create(self, data):
        password = data["password"]
        hashed_password = bcrypt.generate_password_hash(password).decode()
        data["password"] = hashed_password
        instance = self.repository.model(**data)
        return self.repository.add(instance)

    def update(self, id, data):
        return super().update(id, data)

    def get_by_username(self, username: str):
        return self.repository.find_by_username(username)

    def delete(self, id):
        return self.repository.delete_by_id(id)

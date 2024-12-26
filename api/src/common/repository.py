from abc import ABC, abstractmethod
from typing import List, TypeVar, Generic, Type
from sqlalchemy.orm import Session

T = TypeVar("T")
ID = TypeVar("ID")


class AbstractRepository(ABC, Generic[T, ID]):
    def __init__(self, session: Session, model: Type[T]):
        self.session = session
        self.model = model

    @abstractmethod
    def add(self, item: T) -> T:
        """Add a new item to the repository"""
        raise NotImplementedError

    @abstractmethod
    def update(self, item: T) -> T:
        """Update an existing item in the repository"""
        raise NotImplementedError

    @abstractmethod
    def delete_by_id(self, item_id: ID) -> None:
        """Delete an item from the repository by its ID"""
        raise NotImplementedError

    @abstractmethod
    def find_by_id(self, item_id: ID) -> T:
        """Retrieve an item by its ID"""
        raise NotImplementedError

    @abstractmethod
    def find_all(self) -> List[T]:
        """Retrieve all items from the repository"""
        raise NotImplementedError


class SQLAlchemyRepository(AbstractRepository[T, ID]):

    def add(self, item: T) -> T:
        self.session.add(item)
        self.session.commit()
        return item

    def update(self, item: T) -> T:
        self.session.merge(item)
        self.session.commit()
        return item

    def delete_by_id(self, item_id: ID) -> T:
        item = self.find_by_id(item_id)
        if item:
            self.session.delete(item)
            self.session.commit()
        else:
            raise ValueError(f"Item with id {item_id} not found")

    def find_by_id(self, item_id: ID) -> T:
        return self.session.query(self.model).get(item_id)

    def find_all(self) -> List[T]:
        return self.session.query(self.model).all()

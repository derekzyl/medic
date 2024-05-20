from typing import Any, Dict, List, Type

from sqlalchemy.orm import Session


class CrudService:
    def __init__(self, model: Type[Base], schema: Type[BaseSchema], db: Session):
        self.model = model
        self.schema = schema
        self.db = db

    def get_many(self, filter: Dict[str, Any], select: List[str] = None, populate: Dict[str, Any] = {}):
        query = self.db.query(self.model).filter_by(**filter)
        if select:
            query = query.with_entities(*[getattr(self.model, field) for field in select])
        return query.all()

    def get_one(self, data: Dict[str, Any], select: List[str] = None, populate: Dict[str, Any] = {}):
        query = self.db.query(self.model).filter_by(**data)
        if select:
            query = query.with_entities(*[getattr(self.model, field) for field in select])
        return query.first()

    def create(self, data: Dict[str, Any]):
        db_item = self.model(**data)
        self.db.add(db_item)
        self.db.commit()
        self.db.refresh(db_item)
        return db_item

    def update(self, item_id: int, data: Dict[str, Any]):
        db_item = self.db.query(self.model).filter_by(id=item_id).first()
        if db_item:
            for key, value in data.items():
                setattr(db_item, key, value)
            self.db.commit()
            self.db.refresh(db_item)
            return db_item
        return None

    def delete(self, item_id: int):
        db_item = self.db.query(self.model).filter_by(id=item_id).first()
        if db_item:
            self.db.delete(db_item)
            self.db.commit()
            return db_item
        return None
